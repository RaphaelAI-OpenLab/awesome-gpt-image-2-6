"""Source-linked cases: bilingual pages, explicit evidence and local-only media."""
from __future__ import annotations
from i18n import DETAIL_LANGUAGES, detail_language, filename
from presentation import language_nav
from common import GENERATED_MARKER, ROOT, localized, md_link, md_text, md_url, read_json, image_path

LABELS = {
    'official-docs': {'en': 'Official documentation', 'zh-CN': '官方文档'},
    'official-launch': {'en': 'Official launch demo', 'zh-CN': '官方发布演示'},
    'community': {'en': 'Creator-reported model', 'zh-CN': '作者自报模型'},
    'source-only': {'en': 'Original prompt at source', 'zh-CN': '原提示词见来源'},
    'not-public': {'en': 'Prompt not public', 'zh-CN': '提示词未公开'},
    'unverified': {'en': 'Prompt availability unverified', 'zh-CN': '提示词公开状态待核验'},
    'unspecified': {'en': 'Variant unspecified', 'zh-CN': '版本未注明'},
    'accessible': {'en': 'Accessible', 'zh-CN': '可打开'},
    'blocked': {'en': 'Blocked in this browser', 'zh-CN': '当前浏览器被拦截'},
    'unknown': {'en': 'Unknown', 'zh-CN': '未知'},
    'archived': {'en': 'Archived locally', 'zh-CN': '已存入仓库'},
    'partial': {'en': 'Partially archived', 'zh-CN': '部分入库'},
    'failed': {'en': 'Retrieval failed', 'zh-CN': '获取失败'},
}


def read_cases():
    return read_json('content/source-cases.json')


def read_external_cases():
    return read_json('external-sites/source-cases.json')


def visible(cases):
    return [item for item in cases if item['status'] == 'published']


def label(key, language):
    return localized(LABELS.get(key, {'en': key}), language)


def page_path(item, language, *, external=False):
    name = filename(detail_language(language))
    prefix = 'external-sites/' if external else ''
    return f"{prefix}cases/{item['id']}/{name}"


def preview(item):
    return next((m for m in item['media'] if m['path'] and m['kind'] != 'video' and m.get('role', 'output') != 'reference'), None)


def render_detail(item, language, *, external=False):
    if language not in DETAIL_LANGUAGES:
        raise ValueError('Untranslated case details must route to an existing English page')
    zh = language == 'zh-CN'
    choose = lambda en, cn: cn if zh else en
    media_heading = choose('Images / animation files', '图片 / 动画文件') if any(m['kind'] == 'video' for m in item['media']) else choose('Images / GIFs', '图片 / GIF')
    root_prefix = '../../../' if external else '../../'
    home = '../../README.md' if external else ('../../README.zh-CN.md' if zh else '../../README.md')
    back_label = choose('← Back to external website archive', '← 返回外站素材目录') if external else choose('← Back to all cases', '← 返回全部案例')
    lines = [GENERATED_MARKER, '', '# ' + md_text(localized(item['title'], language)), '',
             md_link(back_label, home + '#all-cases'), '']
    lines += [language_nav(language, prefix=root_prefix, detail=True), '',
              '**' + label(item['source']['type'], language) + ' · ' + choose('Source-only; not independently reproduced', '仅核对来源；未独立复现') + '**', '',
              md_text(localized(item['notes'], language)), '',
              '## ' + media_heading, '']
    local_media = [m for m in item['media'] if m['path']]
    if not local_media:
        placeholder = f'{root_prefix}assets/media-placeholder-{language}.svg'
        lines += [f"![{choose('Placeholder, not model output', '占位图，不是模型输出')}]({placeholder})", '',
                  '**' + choose('PLACEHOLDER: media not archived. See the source links and item-level availability notes below.', '占位：素材暂未入库，请查看下方来源链接及逐项获取状态。') + '**', '',
                  md_link(choose('View the work at its original source', '到原始来源查看作品'), item['source']['url']), '']
    for media in item['media']:
        if media['path']:
            local_path = root_prefix + media['path']
            if media['kind'] == 'video':
                lines += [md_link(choose('Open local video file', '打开仓库内视频文件'), local_path), '']
            else:
                lines += [f"![{md_text(localized(media['alt'], language))}]({md_url(local_path)})", '']
            if media.get('role') == 'reference':
                lines += ['**' + choose('Reference/input image, not a generated output.', '参考 / 输入图，不是生成结果。') + '**', '']
        lines += ['- ' + md_link(localized(media['alt'], language), media['source_url']) + ' · ' + media['kind'],
                  '  - ' + choose('Credit: ', '署名：') + md_text(media['rights']['credit']),
                  '  - ' + choose('Reuse: ', '使用条件：') + media['rights']['status'] + '. ' + md_text(localized(media['rights']['note'], language))]
        if media['rights']['evidence_url']:
            lines.append('  - ' + md_link(choose('Provenance / rights evidence', '来源 / 权利依据'), image_path(media['rights']['evidence_url'], root_prefix)))
    if item.get('access'):
        access = item['access']
        lines += ['', '## ' + choose('Source-page and media access', '原帖与素材获取状态'), '',
                  '- ' + choose('Checked: ', '核对日期：') + access['checked_at'] + ' (UTC)',
                  '- ' + choose('Original page: ', '原帖：') + label(access['page_status'], language) + '. ' + md_text(localized(access['page_note'], language)),
                  '- ' + choose('Media: ', '素材：') + label(access['media_status'], language) + '. ' + md_text(localized(access['media_note'], language)),
                  '- ' + md_link(choose('Per-file attempts and results', '逐项尝试与结果'), root_prefix + access['report_path'])]
    lines += ['', '## ' + choose('Original prompt', '原始提示词'), '']
    if item['prompt']['status'] == 'source-only':
        lines += [md_link(label('source-only', language), item['prompt']['url']), '',
                  choose('The source publishes the actual prompt. This repository links to it rather than inventing or republishing the full text. Required inputs and parameters remain at the source.', '来源公开了真实提示词。本仓库链接原文，不伪造或转载完整长提示词；所需输入与参数请在原文查看。')]
    elif item['prompt']['status'] == 'unverified':
        lines += ['**' + label('unverified', language) + '**', '',
                  choose('Public availability of the original prompt has not been verified. The original source is credited below.', '尚未核实原始提示词是否公开。原始来源见下方署名信息。')]
    else:
        lines += ['**' + choose('PLACEHOLDER: prompt not publicly provided.', '占位：原作者未公开提示词。') + '**']
    lines += ['', '## ' + choose('Attribution and verification', '来源与核对信息'), '',
              '- ID: ' + item['id'],
              '- ' + choose('Author: ', '作者：') + md_text(item['source']['author']),
              '- ' + md_link(choose('Original source', '原始来源'), item['source']['url']),
              '- ' + choose('Model: ', '模型：') + item['model']['family'],
              '- ' + choose('Variant: ', '版本：') + ' / '.join(label(v, language) if v == 'unspecified' else v.title() for v in item['model']['variants']),
              '- ' + choose('Evidence: ', '依据：') + md_text(localized(item['model']['evidence'], language)),
              '- ' + choose('Collected: ', '收录：') + item['added_at'] + ' (UTC)',
              '- ' + choose('Source checked: ', '来源核对：') + item['verified_at'] + ' (UTC)', '',
              choose('Attribution does not grant a media license. Repository MIT terms do not cover third-party outputs. Local files record provenance and reuse status; source-attributed does not mean open-licensed.', '标注来源不等于取得素材许可。仓库 MIT 协议不覆盖第三方输出；本地素材逐项记录来源与使用状态，source-attributed 不代表开放许可。'), '']
    return '\n'.join(lines)
