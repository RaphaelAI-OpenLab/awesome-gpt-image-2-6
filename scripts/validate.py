#!/usr/bin/env python3
"""Validate configuration, prompt metadata, assets, and local Markdown links."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

from common import ROOT, is_brand_url, load_data, published, read_json


def schema_errors(value, schema: dict, path: str, root: dict) -> list[str]:
    """Validate the small JSON Schema vocabulary used by content/schema.json."""
    if "$ref" in schema:
        schema = root["$defs"][schema["$ref"].split("/")[-1]]
    errors = []
    types = schema.get("type", [])
    types = [types] if isinstance(types, str) else types
    matches = {
        "null": value is None,
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "boolean": isinstance(value, bool),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
    }
    if types and not any(matches.get(kind, False) for kind in types):
        return [f"{path}: expected {' or '.join(types)}"]
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value is not in the allowed options")
    if isinstance(value, str) and "pattern" in schema and not re.fullmatch(schema["pattern"], value):
        errors.append(f"{path}: invalid format")
    if isinstance(value, dict):
        properties = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}.{key}: missing required field")
        for key, child in value.items():
            if key in properties:
                errors.extend(schema_errors(child, properties[key], f"{path}.{key}", root))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}.{key}: unknown field")
            elif isinstance(schema.get("additionalProperties"), dict):
                errors.extend(schema_errors(child, schema["additionalProperties"], f"{path}.{key}", root))
    if isinstance(value, list) and "items" in schema:
        for index, child in enumerate(value):
            errors.extend(schema_errors(child, schema["items"], f"{path}[{index}]", root))
    return errors


def is_date(value) -> bool:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        dt.date.fromisoformat(value)
        return True
    except ValueError:
        return False


def is_https_url(value) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parts = urlsplit(value)
    except ValueError:
        return False
    return parts.scheme == "https" and bool(parts.hostname) and not parts.username and not re.search(r"[\s<>]", value)


def check_asset(path: str, label: str, errors: list[str], *, allow_remote: bool = True) -> None:
    if not isinstance(path, str) or not path.strip():
        errors.append(f"{label}: expected a non-empty asset path")
        return
    if urlsplit(path).scheme:
        if not allow_remote or not is_https_url(path):
            errors.append(f"{label}: expected a local asset path or HTTPS image URL")
        return
    candidate = (ROOT / path).resolve()
    if not candidate.is_relative_to(ROOT.resolve()):
        errors.append(f"{label}: path must stay inside the repository")
    elif not candidate.is_file():
        errors.append(f"{label}: file does not exist: {path}")


def validate_config(config, errors: list[str]) -> None:
    if not isinstance(config, dict):
        errors.append("site.config.json: expected an object")
        return
    required = {
        "project": ["name", "repository_slug", "repository_owner", "default_branch", "model_family", "official_release_date", "official_url", "model_docs_url", "model_ids"],
        "brand": ["name", "home_url", "gallery_url", "model_page_url", "model_available", "model_support_verified_at"],
        "tracking": ["utm_source", "utm_medium", "utm_campaign"],
        "presentation": ["updated_at", "featured_limit", "featured_case_ids", "latest_limit", "generate_case_pages"],
        "cross_promo": ["enabled", "title", "description", "url", "image_path"],
    }
    for section, fields in required.items():
        if not isinstance(config.get(section), dict):
            errors.append(f"site.config.json.{section}: expected an object")
            continue
        for field in fields:
            if field not in config[section]:
                errors.append(f"site.config.json.{section}.{field}: missing required field")
    if not isinstance(config.get("categories"), list) or not config["categories"]:
        errors.append("site.config.json.categories: expected a non-empty array")
    if errors:
        return
    project, brand, presentation = config["project"], config["brand"], config["presentation"]
    for key in ("name", "repository_slug", "default_branch", "model_family"):
        if not isinstance(project[key], str) or not project[key].strip():
            errors.append(f"project.{key}: expected non-empty text")
    if not isinstance(project["repository_owner"], str) or (project["repository_owner"] and not re.fullmatch(r"[A-Za-z0-9-]+", project["repository_owner"])):
        errors.append("project.repository_owner: use a GitHub username/org, or leave empty for this scaffold")
    if not isinstance(project["repository_slug"], str) or not re.fullmatch(r"[A-Za-z0-9_.-]+", project["repository_slug"]):
        errors.append("project.repository_slug: invalid repository name")
    if not isinstance(brand["name"], str) or not brand["name"].strip():
        errors.append("brand.name: expected non-empty text")
    for label, url in (("brand.home_url", brand["home_url"]), ("project.official_url", project["official_url"]), ("project.model_docs_url", project["model_docs_url"])):
        if not is_https_url(url):
            errors.append(f"{label}: expected an HTTPS URL")
    for key in ("gallery_url", "model_page_url"):
        if brand[key] is not None and not is_https_url(brand[key]):
            errors.append(f"brand.{key}: use a live HTTPS URL or null")
        elif brand[key] and is_https_url(brand["home_url"]) and not is_brand_url(brand[key], config):
            errors.append(f"brand.{key}: must use the brand website domain")
    if not isinstance(brand["model_available"], bool):
        errors.append("brand.model_available: expected true or false")
    if brand["model_support_verified_at"] is not None and not is_date(brand["model_support_verified_at"]):
        errors.append("brand.model_support_verified_at: use YYYY-MM-DD or null")
    if brand["model_available"] and (not brand["model_page_url"] or not is_date(brand["model_support_verified_at"])):
        errors.append("brand.model_available=true requires a live model_page_url and model_support_verified_at")
    if not is_date(project["official_release_date"]):
        errors.append("project.official_release_date: expected YYYY-MM-DD")
    if not isinstance(project["model_ids"], list) or not project["model_ids"] or not all(isinstance(model_id, str) and model_id for model_id in project["model_ids"]):
        errors.append("project.model_ids: expected a non-empty list of official model IDs")
    if set(config["tracking"]) != {"utm_source", "utm_medium", "utm_campaign"}:
        errors.append("tracking: only utm_source, utm_medium, and utm_campaign are configurable")
    for key, value in config["tracking"].items():
        if not isinstance(value, str) or not value.strip():
            errors.append(f"tracking.{key}: expected non-empty text")
    try:
        updated = dt.datetime.fromisoformat(presentation["updated_at"])
        if updated.utcoffset() != dt.timedelta(0):
            raise ValueError("expected UTC timestamp")
    except (TypeError, ValueError):
        errors.append("presentation.updated_at: expected an ISO 8601 UTC timestamp")
    for key in ("featured_limit", "latest_limit"):
        if not isinstance(presentation[key], int) or isinstance(presentation[key], bool) or not 1 <= presentation[key] <= 30:
            errors.append(f"presentation.{key}: expected an integer from 1 to 30")
    if not isinstance(presentation["generate_case_pages"], bool):
        errors.append("presentation.generate_case_pages: expected true or false")
    featured_ids = presentation['featured_case_ids']
    if not isinstance(featured_ids, list) or not all(isinstance(case_id, str) and case_id.strip() for case_id in featured_ids):
        errors.append('presentation.featured_case_ids: expected a list of case IDs')
    elif len(featured_ids) != len(set(featured_ids)):
        errors.append('presentation.featured_case_ids: duplicate case IDs')
    seen = set()
    for index, category in enumerate(config["categories"]):
        label = f"categories[{index}]"
        if not isinstance(category, dict) or not all(key in category for key in ("id", "label", "website_url")):
            errors.append(f"{label}: id, label, and website_url are required")
            continue
        category_id = category["id"]
        if not isinstance(category_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", category_id):
            errors.append(f"{label}.id: expected a lowercase slug")
        elif category_id in seen:
            errors.append(f"{label}.id: duplicate category ID")
        else:
            seen.add(category_id)
        if not isinstance(category["label"], dict) or not all(isinstance(category["label"].get(lang), str) and category["label"][lang].strip() for lang in ("en", "zh-CN")):
            errors.append(f"{label}.label: both en and zh-CN names are required")
        url = category["website_url"]
        if url is not None and (not is_https_url(url) or (is_https_url(brand["home_url"]) and not is_brand_url(url, config))):
            errors.append(f"{label}.website_url: use an exact HTTPS URL on the brand domain, or null")
    promo = config["cross_promo"]
    if not isinstance(promo["enabled"], bool):
        errors.append("cross_promo.enabled: expected true or false")
    if promo["image_path"] is not None and not isinstance(promo["image_path"], str):
        errors.append("cross_promo.image_path: expected an image path or null")
    for field in ("title", "description"):
        if not isinstance(promo[field], dict) or not all(isinstance(promo[field].get(lang), str) for lang in ("en", "zh-CN")):
            errors.append(f"cross_promo.{field}: en and zh-CN string fields are required")
    if promo["enabled"]:
        if not is_https_url(promo["url"]):
            errors.append("cross_promo.url: an enabled campaign requires a real HTTPS URL")
        if isinstance(promo["title"], dict) and not all(isinstance(promo["title"].get(lang), str) and promo["title"][lang].strip() for lang in ("en", "zh-CN")):
            errors.append("cross_promo.title: enabled campaign needs both language titles")
        if promo["image_path"]:
            check_asset(promo["image_path"], "cross_promo.image_path", errors, allow_remote=False)


def validate_prompts(config: dict, prompts: list[dict], errors: list[str], warnings: list[str], *, release: bool) -> None:
    categories = {category["id"] for category in config["categories"]}
    seen = set()
    for index, item in enumerate(prompts):
        label = f"prompts[{index}] ({item['id'] or 'unnamed draft'})"
        if item["id"]:
            if item["id"] in seen:
                errors.append(f"{label}: duplicate ID")
            seen.add(item["id"])
        for section, key in (("source", "url"), ("source", "author_url"), ("rights", "license_url"), ("links", "case_detail_url"), ("links", "generate_url")):
            value = item[section][key]
            if value is not None and not is_https_url(value):
                errors.append(f"{label}.{section}.{key}: use HTTPS or null")
            if value and section == "links" and is_https_url(value) and not is_brand_url(value, config):
                errors.append(f"{label}.{section}.{key}: must point to the brand website")
        date_fields = [("added_at", item["added_at"]), ("source.published_at", item["source"]["published_at"]), ("verification.tested_at", item["verification"]["tested_at"]), ("links.generate_url_verified_at", item["links"]["generate_url_verified_at"])]
        for field, value in date_fields:
            if value is not None and not is_date(value):
                errors.append(f"{label}.{field}: use YYYY-MM-DD or null")
        if item["status"] != "published":
            continue
        for field, value in (("id", item["id"]), ("title.en", item["title"]["en"]), ("prompt", item["prompt"]), ("prompt_language", item["prompt_language"]), ("source.author", item["source"]["author"])):
            if not value.strip():
                errors.append(f"{label}.{field}: required before publishing")
        if item["category"] not in categories:
            errors.append(f"{label}.category: choose an ID from site.config.json")
        if not is_date(item["added_at"]):
            errors.append(f"{label}.added_at: a published entry needs its collection date")
        family = item["model"]["family"]
        if family is not None and family != config["project"]["model_family"]:
            errors.append(f"{label}.model.family: must match this collection's model family")
        model_id = item["model"]["api_model_id"]
        if family is None:
            if model_id or item["model"]["variant"] != "unspecified":
                errors.append(f"{label}.model: an unverified family cannot assert a variant or API ID")
            verification = item["verification"]
            if (verification["status"] != "tested" or not verification["tested_on"].strip()
                    or not all(verification["notes"][lang].strip() for lang in ("en", "zh-CN"))):
                errors.append(f"{label}.verification: an unverified model needs actual execution and bilingual limitations")
            if item["source"]["provenance"] not in ("collected", "adapted") or not item["source"]["url"]:
                errors.append(f"{label}.source: an unverified model needs a source-linked prompt")
        if model_id and model_id not in config["project"]["model_ids"]:
            errors.append(f"{label}.model.api_model_id: not in the configured official model IDs")
        if model_id and not model_id.endswith("-" + item["model"]["variant"]):
            errors.append(f"{label}.model: API ID and variant disagree; leave unknown API IDs null")
        if item["source"]["provenance"] in ("collected", "adapted") and not item["source"]["url"]:
            errors.append(f"{label}.source.url: collected/adapted entries require the original source")
        preview = item["preview"]["path"]
        if item["rights"]["preview"] == "link-only":
            if preview or not item["source"]["url"]:
                errors.append(f"{label}: link-only previews require an empty preview.path and a source URL")
        elif not preview:
            errors.append(f"{label}.preview.path: add a preview, or select rights.preview=link-only")
        if preview and item["rights"]["preview"] == "unknown":
            errors.append(f"{label}.rights.preview: do not embed media without known reuse rights")
        if preview and item["rights"]["preview"] in ("permission", "licensed") and not item["rights"]["license_url"]:
            errors.append(f"{label}.rights.license_url: record preview reuse evidence")
        if preview:
            check_asset(preview, f"{label}.preview.path", errors, allow_remote=False)
            if not item["preview"]["alt"]["en"].strip():
                errors.append(f"{label}.preview.alt.en: describe the preview image")
        for reference_index, reference in enumerate(item["reference_images"]):
            check_asset(reference["path"], f"{label}.reference_images[{reference_index}].path", errors, allow_remote=False)
        if item["verification"]["status"] == "tested" and (not is_date(item["verification"]["tested_at"]) or not item["verification"]["tested_on"].strip()):
            errors.append(f"{label}.verification: tested entries need tested_at and tested_on")
        if item["links"]["generate_url"] and (not config["brand"]["model_available"] or not is_date(item["links"]["generate_url_verified_at"])):
            errors.append(f"{label}.links.generate_url: requires verified model availability and a link verification date")
        for field in ("prompt", "preview"):
            if item["rights"][field] == "unknown":
                target = errors if release else warnings
                target.append(f"{label}.rights.{field}: content terms have not been recorded")


def media_mime(data: bytes) -> str | None:
    """Identify formats from bytes, not URL suffixes or CDN query strings."""
    if data.startswith(b'\x89PNG\r\n\x1a\n'):
        return 'image/png'
    if data.startswith(b'\xff\xd8\xff'):
        return 'image/jpeg'
    if data.startswith(b'RIFF') and data[8:12] == b'WEBP':
        return 'image/webp'
    if data.startswith((b'GIF87a', b'GIF89a')):
        return 'image/gif'
    if data[4:8] == b'ftyp':
        return 'video/mp4'
    if b'<svg' in data[:1024]:
        return 'image/svg+xml'
    return None


def validate_source_cases(config, cases, prompts, errors):
    ids = {item['id'] for item in prompts if item.get('id')}
    categories = {item['id'] for item in config['categories']}
    for index, item in enumerate(cases):
        name = f'source-cases[{index}]'
        if item['id'] in ids:
            errors.append(f'{name}.id: duplicate across source cases or prompts')
        ids.add(item['id'])
        if item['category'] not in categories:
            errors.append(f'{name}.category: unknown category')
        if not is_https_url(item['source']['url']):
            errors.append(f'{name}.source.url: expected original HTTPS source')
        if not item['source']['author'].strip():
            errors.append(f'{name}.source.author: missing author')
        for field in ('title', 'notes'):
            for lang in ('en', 'zh-CN'):
                if not item[field][lang].strip():
                    errors.append(f'{name}.{field}.{lang}: required bilingual text')
        for lang in ('en', 'zh-CN'):
            if not item['model']['evidence'][lang].strip():
                errors.append(f'{name}.model.evidence.{lang}: record explicit model evidence')
        variants = item['model']['variants']
        if not variants or len(variants) != len(set(variants)) or ('unspecified' in variants and len(variants) != 1):
            errors.append(f'{name}.model.variants: record distinct known variants or unspecified alone')
        for field in ('added_at', 'verified_at'):
            if not is_date(item[field]):
                errors.append(f'{name}.{field}: expected ISO date')
        if item['prompt']['status'] == 'source-only':
            if not is_https_url(item['prompt']['url']):
                errors.append(f'{name}.prompt.url: required for public source prompt')
        elif item['prompt']['url'] is not None:
            errors.append(f"{name}.prompt.url: {item['prompt']['status']} prompts must not have a prompt URL")
        entries = item['prompt'].get('entries')
        if entries is not None:
            if item['prompt']['status'] != 'source-only' or not entries:
                errors.append(f'{name}.prompt.entries: original text requires a public source prompt and at least one entry')
            for pindex, entry in enumerate(entries):
                if not entry['text'].strip() or not is_https_url(entry['url']):
                    errors.append(f'{name}.prompt.entries[{pindex}]: original text and HTTPS source are required')
                if not all(entry['title'][lang].strip() for lang in ('en', 'zh-CN')):
                    errors.append(f'{name}.prompt.entries[{pindex}].title: bilingual title required')
                if 'path' in entry:
                    expected_folder = f"cases/{item['id']}/"
                    path = entry['path']
                    if not path.startswith(expected_folder) or '..' in Path(path).parts or not path.endswith('.txt'):
                        errors.append(f'{name}.prompt.entries[{pindex}].path: expected a text file under {expected_folder}')
                    else:
                        check_asset(path, f'{name}.prompt.entries[{pindex}].path', errors, allow_remote=False)
                        prompt_file = ROOT / path
                        if prompt_file.is_file() and prompt_file.read_text(encoding='utf-8') != entry['text'] + '\n':
                            errors.append(f'{name}.prompt.entries[{pindex}].path: text file must exactly match the original prompt plus a final newline')
        if 'note' in item['prompt'] and not all(item['prompt']['note'][lang].strip() for lang in ('en', 'zh-CN')):
            errors.append(f'{name}.prompt.note: bilingual note required')
        access = item.get('access')
        if access:
            if not is_date(access['checked_at']):
                errors.append(f'{name}.access.checked_at: expected ISO date')
            for field in ('page_note', 'media_note'):
                if not all(access[field][lang].strip() for lang in ('en', 'zh-CN')):
                    errors.append(f'{name}.access.{field}: bilingual note required')
            check_asset(access['report_path'], f'{name}.access.report_path', errors, allow_remote=False)
            if access['media_status'] == 'archived' and (not item['media'] or any(not m['path'] for m in item['media'])):
                errors.append(f'{name}.access.media_status: archived requires all recorded media files locally')
        for mindex, media in enumerate(item['media']):
            mname = f'{name}.media[{mindex}]'
            if not is_https_url(media['source_url']):
                errors.append(f'{mname}.source_url: expected original HTTPS asset URL')
            if urlsplit(media['source_url']).path.lower().endswith('.mp4') and media['kind'] != 'video':
                errors.append(f'{mname}.kind: MP4 sources must be labelled video, not GIF/image')
            for lang in ('en', 'zh-CN'):
                if not media['alt'][lang].strip() or not media['rights']['note'][lang].strip():
                    errors.append(f'{mname}: bilingual alt and rights note required')
            if not media['rights']['credit'].strip():
                errors.append(f'{mname}.rights.credit: required')
            path = media['path']
            if media['rights']['status'] == 'link-only':
                if path:
                    errors.append(f'{mname}: link-only media cannot have a local path')
                continue
            if media['rights']['status'] == 'source-attributed':
                if media['rights']['evidence_url'] != item['source']['url']:
                    errors.append(f'{mname}: source-attributed media must retain its exact original source as evidence')
            if not path:
                errors.append(f'{mname}.path: reusable media requires a local file')
                continue
            check_asset(path, f'{mname}.path', errors, allow_remote=False)
            folder = 'references' if media.get('role') == 'reference' else 'examples'
            expected = f"assets/{folder}/{item['id']}/"
            if not path.startswith(expected) or '..' in Path(path).parts:
                errors.append(f'{mname}.path: expected {expected} with no traversal')
            allowed = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg', '.mp4'}
            if Path(path).suffix.lower() not in allowed:
                errors.append(f'{mname}.path: unsupported preview media format')
            evidence = media['rights']['evidence_url']
            if not evidence:
                errors.append(f'{mname}.rights.evidence_url: required reuse evidence')
            elif not is_https_url(evidence):
                check_asset(evidence, f'{mname}.rights.evidence_url', errors, allow_remote=False)
            candidate = ROOT / path
            if candidate.is_file():
                data = candidate.read_bytes()
                if len(data) > 10 * 1024 * 1024:
                    errors.append(f'{mname}.path: individual media must be no larger than 10 MiB')
                if media.get('bytes') != len(data):
                    errors.append(f'{mname}.bytes: must match the local file size')
                if media.get('sha256') != hashlib.sha256(data).hexdigest():
                    errors.append(f'{mname}.sha256: must match the local file checksum')
                mime = media_mime(data)
                if not mime or media.get('mime_type') != mime:
                    errors.append(f'{mname}.mime_type: must match the actual file format')
                suffixes = {'image/png': {'.png'}, 'image/jpeg': {'.jpg', '.jpeg'}, 'image/webp': {'.webp'}, 'image/gif': {'.gif'}, 'image/svg+xml': {'.svg'}, 'video/mp4': {'.mp4'}}
                if mime and Path(path).suffix.lower() not in suffixes[mime]:
                    errors.append(f'{mname}.path: extension must match the actual file format')
                required_kind = {'image/gif': 'gif', 'image/svg+xml': 'svg', 'video/mp4': 'video'}.get(mime)
                if required_kind and media['kind'] != required_kind:
                    errors.append(f'{mname}.kind: must match the actual file format')
                elif mime in ('image/png', 'image/jpeg', 'image/webp') and media['kind'] not in ('image', 'poster'):
                    errors.append(f'{mname}.kind: raster preview must be image or poster')


def markdown_link_errors() -> list[str]:
    errors = []
    anchors = {}
    paths = (list(ROOT.glob("*.md")) + list((ROOT / "docs").glob("*.md"))
             + list((ROOT / "cases").glob("*/README*.md")))
    for path in paths:
        text = path.read_text(encoding="utf-8")
        # Ignore code samples so draft JSON and intentionally shown placeholders are not treated as live links.
        prose = re.sub(r"(?ms)^(`{3,}|~{3,}).*?^\1[^\n]*$", "", text)
        targets = re.findall(r"!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", prose)
        targets += re.findall(r'(?:href|src)="([^"]+)"', prose)
        for raw in targets:
            target = html.unescape(raw)
            if "{{" in target or urlsplit(target).scheme or target.startswith("//"):
                continue
            parts = urlsplit(target)
            linked = (path.parent / unquote(parts.path)).resolve() if parts.path else path
            if not linked.is_relative_to(ROOT.resolve()) or not linked.exists():
                errors.append(f"{path.relative_to(ROOT)}: local link does not exist: {target}")
                continue
            if parts.fragment and linked.suffix == ".md":
                if linked not in anchors:
                    contents = linked.read_text(encoding="utf-8")
                    explicit = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', contents))
                    headings = {re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-") for heading in re.findall(r"^#+ (.+)$", contents, re.M)}
                    anchors[linked] = explicit | headings
                if unquote(parts.fragment) not in anchors[linked]:
                    errors.append(f"{path.relative_to(ROOT)}: local anchor does not exist: {target}")
    return errors


def validate_locales(errors):
    from i18n import LANGUAGES, filename
    if len({filename(language) for language in LANGUAGES}) != len(LANGUAGES):
        errors.append('locales: every language must have a unique README route')
    try:
        english = read_json('content/locales/en.json')['messages']
    except (OSError, KeyError, json.JSONDecodeError) as error:
        errors.append(f'locales: {error}')
        return
    for language in LANGUAGES:
        try:
            data = read_json(f'content/locales/{language}.json')
        except (OSError, json.JSONDecodeError) as error:
            errors.append(f'locales.{language}: {error}')
            continue
        if not isinstance(data, dict) or data.get('language') != language or not isinstance(data.get('messages'), dict):
            errors.append(f'locales.{language}: expected matching language and messages object')
            continue
        messages = data['messages']
        if set(messages) != set(english):
            errors.append(f'locales.{language}: keys must exactly match the English UI catalog')
        for key, value in messages.items():
            if not isinstance(value, str) or not value.strip():
                errors.append(f'locales.{language}: non-empty translation required for {key!r}')
                continue
            if set(re.findall(r"\{[a-zA-Z_][a-zA-Z0-9_]*\}", key)) != set(re.findall(r"\{[a-zA-Z_][a-zA-Z0-9_]*\}", value)):
                errors.append(f'locales.{language}: placeholders differ for {key!r}')
            if key.count('|') != value.count('|'):
                errors.append(f'locales.{language}: table separators differ for {key!r}')
            if language == 'en' and key != value:
                errors.append('locales.en: source text must match its key')


def validate(*, release: bool = False, check_links: bool = True) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    try:
        config, prompts = load_data()
        schema = read_json("content/schema.json")
        template = read_json("templates/prompt.json")
        cases = read_json("content/source-cases.json")
        case_schema = read_json("content/source-cases.schema.json")
        case_template = read_json("templates/source-case.json")
    except (OSError, json.JSONDecodeError) as error:
        return [str(error)], warnings
    validate_config(config, errors)
    validate_locales(errors)
    errors.extend(schema_errors(prompts, schema, "prompts", schema))
    errors.extend(schema_errors([template], schema, "template", schema))
    errors.extend(schema_errors(cases, case_schema, "source-cases", case_schema))
    errors.extend(schema_errors([case_template], case_schema, "source-case-template", case_schema))
    if errors:
        return errors, warnings
    from browse import validate_browse, validate_web_gallery
    validate_browse(cases, errors)
    validate_web_gallery(config, errors)
    validate_source_cases(config, cases, prompts, errors)
    published_case_ids = {item['id'] for item in cases if item['status'] == 'published'}
    unknown_featured = set(config['presentation']['featured_case_ids']) - published_case_ids
    if unknown_featured:
        errors.append(f'presentation.featured_case_ids: unknown or unpublished cases: {sorted(unknown_featured)}')
    from source_cases import is_supported_source
    for item in cases:
        if not is_supported_source(item):
            errors.append(f"{item['id']}: 本仓库仅收录官方、社媒与论坛、内容发布社区及 GitHub 来源")
    validate_prompts(config, prompts, errors, warnings, release=release)
    for asset in ("assets/hero/raphael-gpt-image-2-6-hero-v1.png", "assets/website/gpt-image-2-6-prompts-20261113.jpg", "assets/gallery-placeholder.svg", "assets/media-placeholder-en.svg", "assets/media-placeholder-zh-CN.svg"):
        check_asset(asset, asset, errors, allow_remote=False)
    if release:
        if not published(prompts):
            errors.append("Release: no published prompts yet; this is an intentional empty scaffold")
        if not config["project"]["repository_owner"]:
            errors.append("Release: set project.repository_owner to the actual GitHub owner")
        if not config["brand"]["model_available"]:
            warnings.append("Release: Raphael model support is not marked verified; keep generic homepage CTAs")
    if check_links:
        errors.extend(markdown_link_errors())
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release", action="store_true", help="Also check content-launch readiness; empty scaffolds intentionally fail this mode.")
    args = parser.parse_args()
    errors, warnings = validate(release=args.release)
    for warning in warnings:
        print(f"NOTE: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Validation failed ({len(errors)} issues).", file=sys.stderr)
        return 1
    _, prompts = load_data()
    print(f"Validation passed: {len(published(prompts))} published prompts, {sum(item['status'] == 'draft' for item in prompts)} drafts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
