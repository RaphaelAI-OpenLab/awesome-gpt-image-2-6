#!/usr/bin/env python3
"""Render the English/Chinese README and optional case pages from one dataset."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from common import (
    GENERATED_MARKER, LANGUAGES, ROOT, code_block, html_attr, image_path,
    load_data, localized, md_link, md_text, md_url, published, repo_url, tracked_url,
)

COPY = {
    "en": {
        "intro": "An open collection for GPT Image 2.6 prompts, visual examples, and original sources.",
        "empty_status": "Framework prepared · 0 published prompts",
        "count": "published prompts",
        "empty": "This collection is ready for its first examples. No prompt examples have been published yet.",
        "visit": "Visit {brand} ↗",
        "gallery": "Browse the visual collection on {brand} ↗",
        "model": "View current GPT Image 2.6 options on {brand} ↗",
        "prompts": "Prompt collection",
        "case_gallery": "Source-linked case gallery",
        "case_gallery_note": "Browse verified source examples, original prompts where available, and clearly separated research leads. These are not included in the published-prompt count below.",
        "categories": "Explore by category",
        "latest": "Recently added",
        "featured": "Visual preview",
        "contribute": "Contribute a prompt",
        "using": "How to use this collection",
        "use_steps": [
            "Choose a category and open a prompt card.",
            "Check its source, required reference images, model variant, and test status.",
            "Copy the original prompt and use the recorded settings. If a verified generation link is provided, you can open it directly.",
        ],
        "source_heading": "Sources & contributions",
        "source_text": "Each entry keeps its original source and separates collected examples from our own test results. Prompts remain in their original language. Image and prompt reuse terms are recorded per entry.",
        "contrib_text": "Have an example to add? Follow the contribution guide and include the original post, prompt, and preview credit.",
        "license": "The repository code and original documentation use the MIT license. Third-party prompts and images retain their own terms.",
        "official": "Official model announcement",
        "docs": "Official model documentation",
        "maintainer": "Maintainer guide",
        "empty_category": "No published prompts in this category yet.",
        "empty_latest": "New entries will appear here after they are published.",
        "placeholder_alt": "Three reserved preview slots; these are placeholders, not generated examples",
        "category_column": "Category",
        "count_column": "Published here",
        "date_column": "Added",
        "example_column": "Example",
        "status_column": "Status",
        "tested": "Tested by the curator",
        "source_only": "Collected · not independently tested",
        "prompt": "Original prompt",
        "inputs": "Reference images",
        "workflow": "Workflow",
        "source": "Original source",
        "author": "Author",
        "details": "View case details on {brand}",
        "try": "Try this prompt on {brand}",
        "local_case": "Standalone case page",
        "parameters": "Recorded settings",
        "setting": "Setting",
        "value": "Value",
        "model_family": "Model family",
        "variant": "Variant",
        "unspecified": "Not specified by source",
        "test_notes": "Test notes",
        "notes": "Notes",
        "credit": "Preview credit",
        "rights": "Content terms",
        "view_source_image": "View image at original source",
        "back": "Back to the collection",
        "footer": "Curated by {brand}. Star this repository to follow new additions.",
        "follow": "Follow updates on GitHub",
    },
    "zh-CN": {
        "intro": "收集 GPT Image 2.6 的提示词、效果图与原始来源。",
        "empty_status": "框架已备好 · 0 条已发布提示词",
        "count": "条已发布提示词",
        "empty": "这里预留给后续的真实案例，目前尚未发布提示词。",
        "visit": "访问 {brand} ↗",
        "gallery": "在 {brand} 浏览完整效果合集 ↗",
        "model": "查看 {brand} 当前的 GPT Image 2.6 选项 ↗",
        "prompts": "提示词合集",
        "case_gallery": "案例与原始来源索引",
        "case_gallery_note": "查看已核对来源的案例、原文提示词入口，以及单独标注的待核实线索。这些条目不计入下方已发布提示词数量。",
        "categories": "按用途浏览",
        "latest": "最近收录",
        "featured": "效果预览",
        "contribute": "贡献提示词",
        "using": "如何使用这份合集",
        "use_steps": [
            "选择用途分类，打开提示词卡片。",
            "查看原始来源、所需参考图、模型版本与实测状态。",
            "复制原始提示词，按记录的参数使用；有经过验证的生成链接时，可以直接打开。",
        ],
        "source_heading": "来源与贡献",
        "source_text": "每条记录保留原始来源，并区分收集到的案例与我们自己的实测结果。提示词保留原文，图片与提示词的使用条件逐条记录。",
        "contrib_text": "欢迎提交案例。请按贡献指南附上原始帖子、提示词与图片署名。",
        "license": "仓库代码与原创说明文档采用 MIT 协议；第三方提示词与图片保留各自的使用条件。",
        "official": "模型官方发布说明",
        "docs": "模型官方文档",
        "maintainer": "维护者填充指南",
        "empty_category": "该分类尚未发布提示词。",
        "empty_latest": "新案例发布后会出现在这里。",
        "placeholder_alt": "三个预留效果图位置；这是占位示意，不是模型生成案例",
        "category_column": "分类",
        "count_column": "仓库已发布",
        "date_column": "收录日期",
        "example_column": "案例",
        "status_column": "状态",
        "tested": "整理者已实测",
        "source_only": "来自原帖 · 尚未独立实测",
        "prompt": "原始提示词",
        "inputs": "参考图",
        "workflow": "操作步骤",
        "source": "原始来源",
        "author": "作者",
        "details": "在 {brand} 查看案例详情",
        "try": "在 {brand} 使用这条提示词",
        "local_case": "独立案例页",
        "parameters": "已记录参数",
        "setting": "项目",
        "value": "内容",
        "model_family": "模型系列",
        "variant": "版本",
        "unspecified": "来源未注明",
        "test_notes": "实测说明",
        "notes": "补充说明",
        "credit": "预览图署名",
        "rights": "内容使用条件",
        "view_source_image": "到原始来源查看图片",
        "back": "返回合集",
        "footer": "由 {brand} 整理。可以 Star 仓库，关注后续收录。",
        "follow": "在 GitHub 关注更新",
    },
}


def t(language: str, key: str, **kwargs) -> str:
    return COPY[language][key].format(**kwargs)


def filename(language: str) -> str:
    return "README.md" if language == "en" else "README.zh-CN.md"


def case_path(item: dict, language: str) -> str:
    return f"cases/{item['id']}/{filename(language)}"


def site_link(config: dict, language: str, label: str, url: str, placement: str) -> str:
    return md_link(label, tracked_url(url, placement, language, config))


def status_label(item: dict, language: str) -> str:
    key = "tested" if item["verification"]["status"] == "tested" else "source_only"
    return t(language, key)


def render_gallery(items: list[dict], config: dict, language: str) -> str:
    if not items:
        return f"![{t(language, 'placeholder_alt')}](assets/gallery-placeholder.svg)\n\n{t(language, 'empty')}"
    chosen = [item for item in items if item.get("featured")]
    if not chosen:
        chosen = items
    chosen = chosen[:config["presentation"]["featured_limit"]]
    rows = []
    for start in range(0, len(chosen), 3):
        cells = []
        for item in chosen[start:start + 3]:
            title = localized(item["title"], language)
            destination = "#case-" + item["id"]
            preview = item["preview"].get("path", "")
            if preview:
                visual = f'<img src="{html_attr(preview)}" alt="{html_attr(localized(item["preview"]["alt"], language))}" width="280" />'
            else:
                visual = html_attr(t(language, "view_source_image"))
            cells.append(f'<td width="33%" align="center"><a href="{html_attr(destination)}">{visual}<br /><strong>{html_attr(title)}</strong></a></td>')
        rows.append("<tr>\n" + "\n".join(cells) + "\n</tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def render_case(item: dict, config: dict, language: str, *, standalone: bool = False) -> str:
    prefix = "../../" if standalone else ""
    title = localized(item["title"], language)
    lines = [f'<a id="case-{item["id"]}"></a>', "", f"{'#' if standalone else '####'} {md_text(title)}", ""]
    if standalone:
        lines.extend([md_link(t(language, "back"), prefix + filename(language)), ""])
    lines.extend([f"**{status_label(item, language)}**", ""])
    summary = localized(item.get("summary", {}), language)
    if summary:
        lines.extend([summary, ""])
    preview = item["preview"].get("path", "")
    if preview:
        lines.extend([f"![{md_text(localized(item['preview']['alt'], language))}]({md_url(image_path(preview, prefix))})", ""])
    elif item["source"].get("url"):
        lines.extend([md_link(t(language, "view_source_image"), item["source"]["url"]), ""])
    source = item["source"]
    source_parts = []
    if source.get("url"):
        source_parts.append(md_link(t(language, "source"), source["url"]))
    if source.get("author"):
        author = md_link(source["author"], source["author_url"]) if source.get("author_url") else md_text(source["author"])
        source_parts.append(f"{t(language, 'author')}: {author}")
    if source.get("published_at"):
        source_parts.append(source["published_at"])
    if source_parts:
        lines.extend([" · ".join(source_parts), ""])
    if item["rights"].get("credit"):
        lines.extend([f"{t(language, 'credit')}: {md_text(item['rights']['credit'])}", ""])
    if item["rights"].get("license_url"):
        lines.extend([md_link(t(language, "rights"), item["rights"]["license_url"]), ""])
    lines.extend([f"**{t(language, 'prompt')}**", "", code_block(item["prompt"]), ""])
    model = item["model"]
    variant = model["variant"] if model["variant"] != "unspecified" else t(language, "unspecified")
    settings = [(t(language, "model_family"), model["family"]), (t(language, "variant"), variant)]
    if model.get("api_model_id"):
        settings.append(("API model ID", model["api_model_id"]))
    settings.extend((key, value) for key, value in item["workflow"]["parameters"].items() if value is not None and value != "")
    settings.extend((key, value) for key, value in item["workflow"].get("extra_parameters", {}).items() if value is not None and value != "")
    lines.extend([f"**{t(language, 'parameters')}**", "", f"| {t(language, 'setting')} | {t(language, 'value')} |", "| --- | --- |"])
    lines.extend(f"| {md_text(key)} | {md_text(value)} |" for key, value in settings)
    lines.append("")
    if item.get("reference_images"):
        lines.extend([f"**{t(language, 'inputs')}**", ""])
        for index, reference in enumerate(item["reference_images"], 1):
            description = localized(reference.get("description", {}), language) or f"Reference {index}"
            path = image_path(reference["path"], prefix)
            lines.append(f"{index}. {md_link(description, path)}")
        lines.append("")
    if item["workflow"].get("steps"):
        lines.extend([f"**{t(language, 'workflow')}**", ""])
        lines.extend(f"{index}. {step}" for index, step in enumerate(item["workflow"]["steps"], 1))
        lines.append("")
    verification = item["verification"]
    notes = localized(verification.get("notes", {}), language)
    if verification["status"] == "tested" or notes:
        lines.extend([f"**{t(language, 'test_notes')}**", ""])
        if verification["status"] == "tested":
            lines.extend([f"{md_text(verification['tested_on'])} · {verification['tested_at']}", ""])
        if notes:
            lines.extend([notes, ""])
    extra_notes = localized(item.get("notes", {}), language)
    if extra_notes:
        lines.extend([f"**{t(language, 'notes')}**", "", extra_notes, ""])
    links = item["links"]
    buttons = []
    brand = config["brand"]["name"]
    if not standalone and config["presentation"]["generate_case_pages"]:
        buttons.append(md_link(t(language, "local_case"), case_path(item, language)))
    if links.get("case_detail_url"):
        buttons.append(site_link(config, language, t(language, "details", brand=brand), links["case_detail_url"], f"case_detail_{item['id']}"))
    if config["brand"]["model_available"] and links.get("generate_url") and links.get("generate_url_verified_at"):
        buttons.append(site_link(config, language, t(language, "try", brand=brand), links["generate_url"], f"case_{item['id']}"))
    if buttons:
        lines.extend([" · ".join(buttons), ""])
    return "\n".join(lines).rstrip() + "\n"


def render_readme(config: dict, prompts: list[dict], language: str) -> str:
    items = published(prompts)
    brand = config["brand"]
    project = config["project"]
    lines = [GENERATED_MARKER, ""]
    promo = config["cross_promo"]
    lines.append("<!-- SLOT: cross-promo. Disabled until a real campaign URL is configured. -->")
    if promo["enabled"]:
        link = tracked_url(promo["url"], "cross_promo", language, config)
        lines.extend([f"> **{md_link(localized(promo['title'], language), link)}**", ">", f"> {localized(promo['description'], language)}", ""])
        if promo.get("image_path"):
            lines.extend([f"[![{md_text(localized(promo['title'], language))}]({md_url(promo['image_path'])})]({link})", ""])
    count_text = t(language, "empty_status") if not items else ("1 published prompt" if language == "en" and len(items) == 1 else str(len(items)) + " " + t(language, "count"))
    lines.extend([
        "<!-- SLOT: hero. Clickable brand entry. -->",
        f"[![{md_text(project['name'])}](assets/header.svg)]({tracked_url(brand['home_url'], 'hero', language, config)})",
        "", f"# {md_text(project['name'])}", "", t(language, "intro"), "",
        f"**{count_text}**", "",
        md_link(t(language, "case_gallery"), "docs/CASE_GALLERY.md"), "",
        t(language, "case_gallery_note"), "",
        "[English](README.md) · [简体中文](README.zh-CN.md)", "",
        "<!-- SLOT: top-nav. Website link remains distinct from local navigation. -->",
        " · ".join([
            md_link(t(language, "prompts"), "#collection"),
            md_link(t(language, "case_gallery"), "docs/CASE_GALLERY.md"),
            md_link(t(language, "categories"), "#categories"),
            md_link(t(language, "contribute"), "CONTRIBUTING.md"),
            site_link(config, language, brand["name"] + " ↗", brand["home_url"], "top_nav"),
        ]), "",
        "<!-- SLOT: primary-cta. Use the live gallery when configured; otherwise the live homepage. -->",
    ])
    primary_url = brand.get("gallery_url") or brand["home_url"]
    primary_copy = "gallery" if brand.get("gallery_url") else "visit"
    lines.extend([f"**{site_link(config, language, t(language, primary_copy, brand=brand['name']), primary_url, 'top_cta')}**", ""])
    if brand["model_available"] and brand.get("model_page_url"):
        lines.extend([site_link(config, language, t(language, "model", brand=brand["name"]), brand["model_page_url"], "model_entry"), ""])
    lines.extend([f"## {t(language, 'featured')}", "", render_gallery(items, config, language), "", '<a id="categories"></a>', "", f"## {t(language, 'categories')}", "", "<!-- SLOT: category-links. Local anchors until each exact website_url is configured. -->", f"| {t(language, 'category_column')} | {t(language, 'count_column')} |", "| --- | ---: |"])
    for category in config["categories"]:
        category_id = category["id"]
        url = category.get("website_url")
        destination = tracked_url(url, "category_" + category_id, language, config) if url else "#category-" + category_id
        count = sum(item["category"] == category_id for item in items)
        lines.append(f"| {md_link(localized(category['label'], language), destination)} | {count} |")
    lines.extend(["", f"## {t(language, 'latest')}", ""])
    if not items:
        lines.extend([t(language, "empty_latest"), ""])
    else:
        lines.extend([f"| {t(language, 'date_column')} | {t(language, 'example_column')} | {t(language, 'status_column')} |", "| --- | --- | --- |"])
        for item in items[:config["presentation"]["latest_limit"]]:
            lines.append(f"| {item['added_at']} | {md_link(localized(item['title'], language), '#case-' + item['id'])} | {status_label(item, language)} |")
        lines.append("")
    lines.extend(['<a id="collection"></a>', "", f"## {t(language, 'prompts')}", "", "<!-- SLOT: prompt-cards. Only status=published entries are rendered. -->", ""])
    for category in config["categories"]:
        lines.extend([f'<a id="category-{category["id"]}"></a>', "", f"### {md_text(localized(category['label'], language))}", ""])
        category_items = [item for item in items if item["category"] == category["id"]]
        if not category_items:
            lines.extend([t(language, "empty_category"), ""])
        else:
            for item in category_items:
                lines.extend([render_case(item, config, language).rstrip(), "", "---", ""])
    if brand.get("gallery_url"):
        lines.extend(["<!-- SLOT: collection-bottom. Appears only for a live website gallery. -->", f"**{site_link(config, language, t(language, 'gallery', brand=brand['name']), brand['gallery_url'], 'collection_bottom')}**", ""])
    lines.extend([f"## {t(language, 'using')}", ""])
    lines.extend(f"{index}. {step}" for index, step in enumerate(COPY[language]["use_steps"], 1))
    lines.extend(["", md_link(t(language, "official"), project["official_url"]) + " · " + md_link(t(language, "docs"), project["model_docs_url"]), "", f"## {t(language, 'source_heading')}", "", t(language, "source_text"), "", t(language, "contrib_text"), "", md_link(t(language, "contribute"), "CONTRIBUTING.md") + " · " + md_link(t(language, "maintainer"), "docs/FILLING_GUIDE.zh-CN.md"), "", t(language, "license"), "", "---", "", "<!-- SLOT: footer. Persistent brand attribution and site entry. -->", t(language, "footer", brand=brand["name"]), "", site_link(config, language, t(language, "visit", brand=brand["name"]), brand["home_url"], "footer")])
    repository = repo_url(config)
    if repository:
        lines.extend(["", md_link(t(language, "follow"), repository)])
    return "\n".join(lines).rstrip() + "\n"


def outputs(config: dict, prompts: list[dict]) -> dict[Path, str]:
    result = {ROOT / filename(language): render_readme(config, prompts, language) for language in LANGUAGES}
    if config["presentation"]["generate_case_pages"]:
        for item in published(prompts):
            for language in LANGUAGES:
                result[ROOT / case_path(item, language)] = GENERATED_MARKER + "\n\n" + render_case(item, config, language, standalone=True)
    return result


def stale_case_pages(expected: dict[Path, str]) -> list[Path]:
    return [
        path for path in (ROOT / "cases").glob("*/README*.md")
        if path not in expected and path.read_text(encoding="utf-8").startswith(GENERATED_MARKER)
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report stale generated files without changing them.")
    args = parser.parse_args()
    from validate import validate
    errors, _ = validate(check_links=False)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    config, prompts = load_data()
    expected = outputs(config, prompts)
    stale = stale_case_pages(expected)
    changed = [path for path, content in expected.items() if not path.exists() or path.read_text(encoding="utf-8") != content]
    if args.check:
        for path in changed + stale:
            print(f"OUTDATED: {path.relative_to(ROOT)}")
        if changed or stale:
            print("Run: python3 scripts/build_readme.py")
            return 1
        print(f"Generated files are current ({len(expected)} files; {len(published(prompts))} published prompts).")
        return 0
    for path, content in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    for path in stale:
        path.unlink()
        if not any(path.parent.iterdir()):
            path.parent.rmdir()
    print(f"Built {len(expected)} files; {len(published(prompts))} published prompts. Drafts are excluded from rendered pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
