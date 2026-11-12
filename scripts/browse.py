"""按使用场景、风格和主题生成可展开的案例导航。"""
import random

from common import html_attr, localized, md_link, read_json
from i18n import ui


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


def render_browse(cases, language):
    by_id = {item['id']: item for item in cases}
    lines = []
    for group in read_browse():
        sections = []
        for item in group['items']:
            members = [by_id[case_id] for case_id in item['case_ids'] if case_id in by_id]
            if not members:
                continue
            displayed, remaining = members, []
            if group['id'] == 'use-cases' and len(members) > 3:
                # 固定种子随机抽样，保证多语言一致、重复生成和 CI 检查稳定。
                displayed = random.Random(f'{group["id"]}:{item["id"]}').sample(members, 3)
                displayed_ids = {case['id'] for case in displayed}
                remaining = [case for case in members if case['id'] not in displayed_ids]
            title = ui(item['label']['en'], item['label']['zh-CN'], language)
            sections += ['<details open>', '<summary>' + html_attr(title) + '</summary>', '']
            sections += ['- ' + md_link(localized(case['title'], language), '#source-case-' + case['id']) for case in displayed]
            if remaining:
                more = ui('Show {count} more cases', '展开其余 {count} 个案例', language).format(count=len(remaining))
                sections += ['', '<details>', '<summary>' + html_attr(more) + '</summary>', '']
                sections += ['- ' + md_link(localized(case['title'], language), '#source-case-' + case['id']) for case in remaining]
                sections += ['', '</details>', '']
            sections += ['', '</details>', '']
        if sections:
            title = ui(group['label']['en'], group['label']['zh-CN'], language)
            lines += ['### ' + title, ''] + sections
    return '\n'.join(lines)
