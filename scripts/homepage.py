"""README layout inspired by YouMind; all copy and rendering are project-specific."""
from common import GENERATED_MARKER, html_attr, localized, md_link, md_text, published, repo_url, tracked_url
from source_cases import label, page_path, preview, read_cases, visible


def render_home(config, prompts, language, render_prompt):
    zh = language == 'zh-CN'
    c = lambda en, cn: cn if zh else en
    cases = visible(read_cases())
    full = published(prompts)
    brand = config['brand']
    repository = repo_url(config)
    title = config['project']['name']
    def heading(anchor, en, cn):
        return [f'<a id="{anchor}"></a>', '', '## ' + c(en, cn), '']
    def case_link(item):
        return md_link(localized(item['title'], language), page_path(item, language))
    lines = [GENERATED_MARKER, '', f'[![{title}](assets/header.svg)]({tracked_url(brand["home_url"], "hero", language, config)})', '',
             '# 🎨 ' + title, '',
             c('An open collection of prompts, visual examples and original sources for GPT Image 2.6.', 'GPT Image 2.6 提示词、创意案例与原始来源合集。'), '',
             md_link('MIT · ' + c('code & original docs', '代码与原创文档'), 'LICENSE') + ' · ' + md_link(c('Contributions welcome', '欢迎贡献'), 'CONTRIBUTING.md') + (' · ' + md_link(c('Validation CI', '自动校验'), repository + '/actions') if repository else ''), '',
             '⚠️ **' + c('Copyright notice', '版权声明') + c('**: ', '**：') + c('The prompts and media in this collection are gathered from public sources for educational purposes only. If you believe any content infringes your rights, please ', '本仓库的提示词与素材均收集自公开来源，仅供教育目的使用。如果您认为任何内容侵犯了您的权利，请') + md_link(c('open an issue', '提交 issue'), repository + '/issues/new') + c(', and we will remove it immediately.', '，我们将立即移除。'), '',
             '[English](README.md) · [简体中文](README.zh-CN.md)', '', '---', '']
    lines += heading('gallery', '🌐 Browse the collection', '🌐 浏览案例图库')
    lines += ['**' + md_link(c('Browse all cases in this repository →', '浏览仓库内全部案例 →'), '#all-cases') + '**', '',
              c('Every case below opens an internal detail page with model evidence, source credits and prompt availability.', '下方每条案例都链接到仓库内部详情页，包含模型依据、来源署名与提示词状态。'), '']
    if brand.get('gallery_url'):
        lines += [md_link(c('Open the web gallery', '打开网页图库'), tracked_url(brand['gallery_url'], 'top_cta', language, config)), '']
    else:
        lines += ['**' + c('PLACEHOLDER · External web gallery URL: not configured.', '占位 · 外部网页图库链接：待配置。') + '**', '']
    if brand.get('model_page_url') and brand.get('model_available'):
        lines += [md_link(c('Verified model entry', '已核验模型入口'), tracked_url(brand['model_page_url'], 'model_entry', language, config)), '']
    else:
        lines += ['**' + c('PLACEHOLDER · One-click generation link: not verified.', '占位 · 一键生成链接：待核验。') + '**', '']
    promo=config['cross_promo']
    if promo['enabled']:
        lines += [md_link(localized(promo['title'],language),tracked_url(promo['url'],'cross_promo',language,config)), localized(promo['description'],language), '']
        if promo['image_path']:lines += [f"![{md_text(localized(promo['title'],language))}]({promo['image_path']})",'']
    else:
        lines += [c('PLACEHOLDER · Related collection / campaign link: to be added.', '占位 · 关联项目 / 活动链接：待补充。'), '']
    lines += [md_link(c('Visit Raphael (homepage)', '访问 Raphael（主页）'), tracked_url(brand['home_url'], 'top_nav', language, config)), '']
    lines += heading('categories', '🏷️ Browse by category', '🏷️ 按分类浏览')
    lines += ['| ' + c('Category | Source-linked cases | Full prompts', '分类 | 来源案例 | 完整提示词') + ' |', '| --- | ---: | ---: |']
    for category in config['categories']:
        count=sum(x['category']==category['id'] for x in cases)
        full_count=sum(x['category']==category['id'] for x in full)
        lines += [f"| {md_link(localized(category['label'],language),'#category-'+category['id'])} | {count} | {full_count} |"]
    lines += [''] + heading('contents', '📖 Contents', '📖 目录')
    for anchor,en,cn in [('about','What is GPT Image 2.6?','什么是 GPT Image 2.6？'),('statistics','Statistics','统计数据'),('featured','Featured cases','精选案例'),('latest','Recently added','最近收录'),('all-cases','All cases','全部案例'),('collection','Full prompts','完整提示词'),('using','How to use','如何使用'),('contribute','Contribute','如何贡献'),('license','License','许可证'),('acknowledgements','Acknowledgements','致谢'),('star-history','Star history','Star 历史')]:
        lines.append('- '+md_link(c(en,cn),'#'+anchor))
    lines += [''] + heading('about','🤔 What is GPT Image 2.6?','🤔 什么是 GPT Image 2.6？')
    lines += [c('OpenAI introduced Images 2.6 on November 4, 2026. This collection covers the Sunburst and Flare model variants, image creation and editing, plus documented SVG and GIF workflows. Variant support is recorded per case rather than assumed.', 'OpenAI 于 2026 年 11 月 4 日发布 Images 2.6。本合集记录 Sunburst 与 Flare 版本的图片生成、编辑，以及官方展示的 SVG 与 GIF 工作流；具体支持情况按每个案例记录，不作推定。'), '',
              md_link(c('Official announcement','官方发布说明'),config['project']['official_url'])+' · '+md_link(c('Model documentation','模型文档'),config['project']['model_docs_url']), '']
    lines += heading('statistics','📊 Statistics','📊 统计数据')
    metrics=[(c('Source-linked cases','来源案例'),len(cases)),(c('Official examples','官方案例'),sum(x['source']['type'].startswith('official') for x in cases)),(c('Creator-reported examples','社区作者自报案例'),sum(x['source']['type']=='community' for x in cases)),(c('Original prompts available at source','来源公开原始提示词'),sum(x['prompt']['status']=='source-only' for x in cases)),(c('Full prompts published here','仓库内完整提示词'),len(full)),(c('Locally archived media files','本地收录素材文件'),sum(bool(m['path']) for x in cases for m in x['media'])+sum(bool(x['preview']['path']) for x in full)),(c('Last source check (UTC)','最近来源核对（UTC）'),max((x['verified_at'] for x in cases), default='—'))]
    lines += ['| '+c('Metric | Count / date','项目 | 数量 / 日期')+' |','| --- | ---: |']+[f'| {name} | **{value}** |' for name,value in metrics]+['',c('Source counts are not reproduction claims. Pending leads are excluded; different outputs within one workflow count as one case.', '来源数量不代表复现次数。待核实线索不计入案例总数，同一工作流的多个输出合并计数。'),'']
    lines += heading('featured','🔥 Featured cases','🔥 精选案例')
    selected=([x for x in cases if x['featured']] or cases)[:config['presentation']['featured_limit']]
    if selected:
        lines += ['<table>']
        for start in range(0,len(selected),3):
            lines += ['<tr>']
            for item in selected[start:start+3]:
                m=preview(item);path=m['path'] if m else f'assets/media-placeholder-{language}.svg'
                alt=localized(m['alt'],language) if m else c('Placeholder, not model output','占位图，不是模型输出')
                lines += [f'<td width="33%" align="center"><a href="{page_path(item,language)}"><img src="{html_attr(path)}" alt="{html_attr(alt)}" width="280" /><br /><strong>{html_attr(localized(item["title"],language))}</strong></a><br />{html_attr(label(item["source"]["type"],language))}</td>']
            lines += ['</tr>']
        lines += ['</table>','']
    else:lines += [c('No source-linked cases published yet.','尚未发布来源案例。'),'']
    lines += [c('Placeholder cards are not generated results. All displayed media files live in this repository; media not yet archived stays linked on the detail pages.', '占位卡片不是生成结果。展示素材均使用仓库本地文件；暂未入库的原素材在详情页保留来源链接；已入库素材逐条注明授权状态，未确认许可证的不标为开放许可。'),'']
    lines += heading('latest','🆕 Recently added','🆕 最近收录')
    lines += ['| '+c('Added | Case | Evidence','收录日期 | 案例 | 依据')+' |','| --- | --- | --- |']
    # Entries append to the dataset; preserve collection order within one UTC date.
    latest = sorted(enumerate(cases), key=lambda pair: (pair[1]['added_at'], pair[0]), reverse=True)
    for _, item in latest[:config['presentation']['latest_limit']]:
        lines += [f"| {item['added_at']} | {case_link(item)} | {label(item['source']['type'],language)} |"]
    lines += ['']+heading('all-cases','📋 All cases','📋 全部案例')
    for category in config['categories']:
        lines += [f'<a id="category-{category["id"]}"></a>','', '### '+localized(category['label'],language),'']
        group=[x for x in cases if x['category']==category['id']]
        if group:
            lines += ['| '+c('Case · internal detail page | Source | Prompt','案例 · 仓库内部详情 | 来源类型 | 提示词')+' |','| --- | --- | --- |']
            for item in group:lines += [f"| {case_link(item)} | {label(item['source']['type'],language)} | {label(item['prompt']['status'],language)} |"]
            lines += ['']
        else:lines += [c('No source-linked cases in this category yet.','此分类尚无来源案例。'),'']
    lines += [md_link(c('Search log, media report and unresolved leads','检索记录、媒体报道与待核实线索'),'docs/CASE_GALLERY.md'),'']
    lines += heading('collection','📝 Full prompts','📝 完整提示词')
    if full:
        for item in full:lines += [render_prompt(item,config,language).rstrip(),'','---','']
    else:lines += [c('No full prompts are republished here yet. Case pages link to the actual original prompts when public and explicitly mark missing prompts. A source-link entry is not a copyable-prompt entry.', '目前未在仓库转载完整提示词。案例页会链接已公开原文，并明确标注未公开的提示词。来源索引不会冒充可复制提示词。'),'']
    lines += heading('using','📚 How to use','📚 如何使用')
    lines += ['1. '+c('Open a case from a category or featured card.','从分类或精选卡片进入案例。'),'2. '+c('Read its model evidence, required inputs, source and reuse limits.','查看模型依据、必需输入、原始来源与素材使用限制。'),'3. '+c('Follow the original prompt link when available. A missing prompt stays missing; do not infer it from an image.','有原始提示词时前往来源阅读。没有公开提示词时保持缺失，不根据图片臆造。'),'']
    lines += heading('contribute','🤝 How to contribute','🤝 如何贡献')
    lines += [c('Add source-linked cases to content/source-cases.json. Add complete, reusable prompts to content/prompts.json. The generator creates both languages and internal pages from these datasets.', '来源案例写入 content/source-cases.json；取得可收录的完整提示词后写入 content/prompts.json。生成器统一构建双语 README 与仓库内部详情页。'),'',
              md_link(c('Contribution guide','贡献指南'),'CONTRIBUTING.md')+' · '+md_link(c('Source case and media guide','案例与素材维护指南'),'docs/SOURCE_CASES.md')+' · '+md_link(c('Maintainer guide (Chinese)','维护者填充指南'),'docs/FILLING_GUIDE.zh-CN.md'),'']
    lines += heading('license','📄 License','📄 许可证')
    lines += [c('Code, original documentation and decorative SVG placeholders use MIT. Third-party prompts and media retain their own terms and have item-level provenance and reuse status. The adapted README layout is credited separately below.', '代码、原创说明与装饰性 SVG 占位图采用 MIT。第三方提示词及素材保留各自条款，逐项记录来源与使用状态。改编的 README 结构另见下方署名。'),'',md_link(c('Repository license','仓库许可证'),'LICENSE'),'']
    lines += heading('acknowledgements','🙏 Acknowledgements','🙏 致谢')
    lines += [c('README structure adapted from YouMind OpenLab’s awesome-nano-banana-pro-prompts under CC BY 4.0. Adapted for GPT Image 2.6 with new copy, data, local detail pages and explicit placeholders; no creative examples or media were copied.', 'README 结构参考并改编自 YouMind OpenLab 的 awesome-nano-banana-pro-prompts（CC BY 4.0）。已替换为 GPT Image 2.6 的文案、数据、仓库内详情页与明确占位符；未复制其创意案例或图片素材。'),'',
              md_link('YouMind README','https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts/blob/main/README_zh.md')+' · '+md_link('CC BY 4.0','https://creativecommons.org/licenses/by/4.0/')+' · '+md_link(c('Attribution notes','署名说明'),'docs/ATTRIBUTION.md'),'',c('Thanks to OpenAI and the original creators credited on each case page.','感谢 OpenAI 与各案例详情页标注的原作者。'),'']
    lines += heading('star-history','⭐ Star history','⭐ Star 历史')
    lines += ['**'+c('PLACEHOLDER · Star-history chart not configured.','占位 · Star 历史图表尚未配置。')+'**','']
    if repository:lines += [md_link(c('Star / follow this repository','Star / 关注本仓库'),repository),'']
    lines += ['---','',c('Curated by Raphael.','由 Raphael 整理。')+' '+md_link(c('Homepage','主页'),tracked_url(brand['home_url'],'footer',language,config)),'',
              c('Generated from structured source data. Edit the datasets and regenerate; do not edit this file directly.','由结构化数据自动生成。请修改数据源并重新生成，不直接编辑本文件。'),'']
    return '\n'.join(lines)
