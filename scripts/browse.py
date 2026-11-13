"""维护内部案例分类，并生成带数量的网站标签导航。"""
import datetime as dt
from urllib.parse import urlsplit, urlunsplit

from common import is_brand_url, md_link, read_json, tracked_url
from i18n import ui


GALLERY_LANGUAGE_PREFIXES = {
    'en': '', 'zh-CN': 'zh', 'zh-TW': 'zh-Hant',
    'ja-JP': 'ja', 'ko-KR': 'ko', 'th-TH': 'th', 'vi-VN': 'vi',
    'hi-IN': 'hi', 'es-ES': 'es', 'es-419': 'es', 'de-DE': 'de',
    'fr-FR': 'fr', 'it-IT': 'it', 'pt-BR': 'pt', 'pt-PT': 'pt',
    'tr-TR': 'tr',
}


def read_browse():
    return read_json('content/browse.json')


def validate_browse(cases, errors):
    try:
        groups = read_browse()
    except (OSError, ValueError) as error:
        errors.append(f'content/browse.json: {error}')
        return
    expected_groups = ['use-cases', 'styles', 'themes']
    if not isinstance(groups, list) or len(groups) != len(expected_groups):
        errors.append('content/browse.json: expected use cases, styles and themes')
        return
    published_ids = {item['id'] for item in cases if item['status'] == 'published'}
    scene_ids = set()
    for group, expected_id in zip(groups, expected_groups):
        if not isinstance(group, dict) or group.get('id') != expected_id:
            errors.append(f'content/browse.json: expected group {expected_id}')
            continue
        items = group.get('items')
        if not isinstance(items, list) or not items:
            errors.append(f'browse.{expected_id}: non-empty subcategories required')
            continue
        labels = [group.get('label')]
        item_ids = set()
        for item in items:
            if not isinstance(item, dict) or not isinstance(item.get('id'), str) or not item['id']:
                errors.append(f'browse.{expected_id}: subcategory ID required')
                continue
            name = f'browse.{expected_id}.{item["id"]}'
            if item['id'] in item_ids:
                errors.append(f'{name}: duplicate subcategory ID')
            item_ids.add(item['id'])
            labels.append(item.get('label'))
            members = item.get('case_ids')
            if not isinstance(members, list) or not members or not all(isinstance(x, str) for x in members):
                errors.append(f'{name}: non-empty case IDs required')
                continue
            if len(members) != len(set(members)):
                errors.append(f'{name}: duplicate case IDs')
            unknown = set(members) - published_ids
            if unknown:
                errors.append(f'{name}: unknown or unpublished case IDs: {sorted(unknown)}')
            if expected_id == 'use-cases':
                scene_ids.update(members)
        for label in labels:
            if not isinstance(label, dict) or not all(isinstance(label.get(lang), str) and label[lang].strip() for lang in ('en', 'zh-CN')):
                errors.append(f'browse.{expected_id}: bilingual labels required')
    if published_ids - scene_ids:
        errors.append(f'browse.use-cases: missing cases: {sorted(published_ids - scene_ids)}')


def read_web_gallery():
    return read_json('content/web-gallery.json')


def validate_web_gallery(config, errors):
    def valid_url(url):
        try:
            return isinstance(url, str) and urlsplit(url).scheme == 'https' and is_brand_url(url, config)
        except ValueError:
            return False

    if not valid_url(config['brand'].get('gallery_url')):
        errors.append('brand.gallery_url: website navigation requires an HTTPS URL on the brand domain')
    for category in config['categories']:
        if not valid_url(category.get('website_url')):
            errors.append(f'categories.{category["id"]}.website_url: website navigation requires an HTTPS URL on the brand domain')
    try:
        gallery = read_web_gallery()
    except (OSError, ValueError) as error:
        errors.append(f'content/web-gallery.json: {error}')
        return
    if not isinstance(gallery, dict):
        errors.append('content/web-gallery.json: expected an object')
        return
    source = gallery.get('source_url')
    if not valid_url(source):
        errors.append('web-gallery.source_url: expected an HTTPS URL on the brand domain')
    verified_at = gallery.get('verified_at')
    try:
        if dt.date.fromisoformat(verified_at).isoformat() != verified_at:
            raise ValueError('expected ISO date')
    except (TypeError, ValueError):
        errors.append('web-gallery.verified_at: expected YYYY-MM-DD')
    if not isinstance(gallery.get('total'), int) or isinstance(gallery['total'], bool) or gallery['total'] < 0:
        errors.append('web-gallery.total: expected a non-negative integer')
    categories = gallery.get('categories')
    if not isinstance(categories, list):
        errors.append('web-gallery.categories: expected an array')
        return
    expected_ids = {category['id'] for category in config['categories']}
    seen = set()
    for index, category in enumerate(categories):
        name = f'web-gallery.categories[{index}]'
        if not isinstance(category, dict):
            errors.append(f'{name}: expected an object')
            continue
        category_id = category.get('id')
        if not isinstance(category_id, str) or category_id not in expected_ids:
            errors.append(f'{name}.id: expected a configured category ID')
        elif category_id in seen:
            errors.append(f'{name}.id: duplicate category ID')
        else:
            seen.add(category_id)
        label = category.get('label')
        if not isinstance(label, dict) or not all(isinstance(label.get(lang), str) and label[lang].strip() for lang in ('en', 'zh-CN')):
            errors.append(f'{name}.label: bilingual labels required')
        count = category.get('count')
        if not isinstance(count, int) or isinstance(count, bool) or count < 0:
            errors.append(f'{name}.count: expected a non-negative integer')
    if seen != expected_ids:
        errors.append('web-gallery.categories: must include every configured category exactly once')


def gallery_url_for_language(url, language):
    """为已核验的图库规范地址添加网站语言前缀，保留查询参数与锚点。"""
    parts = urlsplit(url)
    prefix = GALLERY_LANGUAGE_PREFIXES[language]
    path = '/' + '/'.join(part for part in (prefix, parts.path.lstrip('/')) if part)
    return urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.fragment))


def render_browse(config, language):
    gallery = read_web_gallery()
    urls = {category['id']: category['website_url'] for category in config['categories']}
    all_url = gallery_url_for_language(config['brand']['gallery_url'], language)
    links = [md_link(ui('All', '全部', language) + f' ({gallery["total"]})',
                     tracked_url(all_url, 'category_all', language, config))]
    for category in gallery['categories']:
        title = ui(category['label']['en'], category['label']['zh-CN'], language)
        url = gallery_url_for_language(urls[category['id']], language)
        links.append(md_link(title + f' ({category["count"]})',
                             tracked_url(url, 'category_' + category['id'], language, config)))
    return ' · '.join(links)
