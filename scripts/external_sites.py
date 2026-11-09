"""按来源网站组织独立存放的外站案例。"""
from collections import defaultdict
from urllib.parse import urlsplit

from common import GENERATED_MARKER, localized, md_link, md_text
from source_cases import label, page_path, visible


# 官方、社媒/论坛、内容发布社区和 GitHub 示例保留在主合集。
PRIMARY_SOURCE_HOSTS = {
    'openai.com', 'developers.openai.com', 'x.com', 'twitter.com',
    'news.ycombinator.com', 'reddit.com', 'github.com', 'note.com',
    'tianqi.csdn.net',
}


def is_external_site(item):
    host = (urlsplit(item['source']['url']).hostname or '').removeprefix('www.')
    return host not in PRIMARY_SOURCE_HOSTS


def render_external_index(cases):
    cases = visible(cases)
    grouped = defaultdict(list)
    for item in cases:
        grouped[urlsplit(item['source']['url']).hostname].append(item)
    files = sum(bool(media['path']) for item in cases for media in item['media'])
    linked = sum(not media['path'] for item in cases for media in item['media'])
    lines = [GENERATED_MARKER, '', '# 外站素材目录', '',
             md_link('返回主合集', '../README.zh-CN.md'), '',
             '本目录单独收录其他独立网站的案例，按直接收录来源网站整理。案例、素材与数据均已移入本目录，不计入主合集的分类、精选、最近收录及统计。', '',
             '官方、社媒与论坛、内容发布社区及 GitHub 示例仓库保留在主合集。提示词状态与原文链接、作者署名、模型依据及素材使用状态按原记录保留。', '',
             f'共 **{len(cases)} 个案例**，来自 **{len(grouped)} 个网站主机**，包含 **{files} 个本地素材文件**及 **{linked} 条仅链接媒体记录**。', '',
             '## 存储位置', '',
             '- `source-cases.json`：本目录案例的数据源，保留原用途分类作为历史元数据。',
             '- `cases/<id>/`：案例的中英文详情页。',
             '- `assets/examples/<id>/`：输出素材。',
             '- `assets/references/<id>/`：参考输入。',
             '- `source-classification.json`：与原始来源分类表对应的案例清单及来源歧义。', '']
    conflicts = {'kavel-open-late', 'kavel-tram', 'kavel-90s-snapshot'}
    conflicted = [item for item in cases if item['id'] in conflicts]
    if conflicted:
        lines += ['## 来源表述有冲突的案例', '',
                  '以下案例的直接收录页与文件服务器为 Kavel，但页面概述称其为 X 帖子，逐素材记录称 Kavel 生成。此次按直接收录页移入外站目录，保留原有冲突说明，不重新认定原作者。', '']
        for item in conflicted:
            lines.append('- ' + md_link(localized(item['title'], 'zh-CN'), page_path(item, 'zh-CN')))
    lines += ['', '## 来源网站', '', '| 来源页主机 | 案例数 | 本地素材文件数 |', '| --- | ---: | ---: |']
    for index, (host, items) in enumerate(sorted(grouped.items()), 1):
        count = sum(bool(media['path']) for item in items for media in item['media'])
        lines.append(f'| {md_link(host, "#site-" + str(index))} | {len(items)} | {count} |')
    lines += ['', '<a id="all-cases"></a>', '', '## 全部外站案例', '']
    for index, (host, items) in enumerate(sorted(grouped.items()), 1):
        lines += [f'<a id="site-{index}"></a>', '', '### ' + host, '',
                  '| 案例 | 来源作者 | 本地文件数 | 提示词状态 | 原始来源 |', '| --- | --- | ---: | --- | --- |']
        for item in items:
            route = page_path(item, 'zh-CN')
            count = sum(bool(media['path']) for media in item['media'])
            lines.append(f"| {md_link(localized(item['title'], 'zh-CN'), route)} | {md_text(item['source']['author'])} | {count} | {label(item['prompt']['status'], 'zh-CN')} | {md_link('查看来源', item['source']['url'])} |")
        lines.append('')
    lines += ['## 维护', '',
              '修改本目录的数据源后，在仓库根目录执行 `python3 scripts/build_readme.py`，同步生成目录和详情页。运行 `python3 scripts/validate.py` 检查素材校验和、来源、跨合集 ID 和本地链接。', '',
              '标注来源不等于取得转载许可。第三方素材继续保留逐项使用状态，不因移动目录而改变授权范围。', '']
    return '\n'.join(lines)
