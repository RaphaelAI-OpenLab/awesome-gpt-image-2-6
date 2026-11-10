# Languages and presentation / 多语言与仓库呈现

[English home](../README.md) · [简体中文首页](../README.zh-CN.md) · [贡献指南](../CONTRIBUTING.md)

## Scope / 翻译范围

The README interface is available in 16 real language editions. Each has its own generated file, translated navigation, headings, explanatory text, category labels, status labels and copyright notice. Native language names appear on local SVG badges; a check mark and color identify the current edition.

README 界面提供 16 个真实语言版本，每种语言都有独立生成文件，翻译导航、标题、说明、分类、状态与版权声明。语言按钮使用本地 SVG，以本语言名称显示；当前版本通过勾选符号与颜色同时标识。

| Locale | Edition |
| --- | --- |
| en | [English](../README.md) |
| zh-CN | [简体中文](../README.zh-CN.md) |
| zh-TW | [繁體中文](../README.zh-TW.md) |
| ja-JP | [日本語](../README.ja-JP.md) |
| ko-KR | [한국어](../README.ko-KR.md) |
| th-TH | [ไทย](../README.th-TH.md) |
| vi-VN | [Tiếng Việt](../README.vi-VN.md) |
| hi-IN | [हिन्दी](../README.hi-IN.md) |
| es-ES | [Español](../README.es-ES.md) |
| es-419 | [Español (Latinoamérica)](../README.es-419.md) |
| de-DE | [Deutsch](../README.de-DE.md) |
| fr-FR | [Français](../README.fr-FR.md) |
| it-IT | [Italiano](../README.it-IT.md) |
| pt-BR | [Português (Brasil)](../README.pt-BR.md) |
| pt-PT | [Português](../README.pt-PT.md) |
| tr-TR | [Türkçe](../README.tr-TR.md) |

**Case content is not claimed to be translated into all 16 languages.** Full case detail pages currently exist in English and Simplified Chinese. Other README editions explicitly disclose their English fallback for case titles, descriptions and detail links. Original prompts, quotations, model names, source URLs and creator names are preserved. No link points to a nonexistent translated detail page.

**不声称案例正文已经翻译成 16 种语言。** 完整案例详情目前只有英文和简体中文；其他 README 明确说明案例标题、描述与详情使用英文回退。原始提示词、引文、模型名称、来源地址和作者名称保持原样，不链接不存在的译文详情。

## Maintain the source / 维护生成源

- `scripts/i18n.py` defines supported locales and unique README filenames. `DETAIL_LANGUAGES` is deliberately separate from interface languages.
- `content/locales/en.json` is the source-keyed UI catalog. Every other locale file must contain exactly the same keys, valid text, matching placeholders such as `{brand}`, and table delimiters.
- Change interface copy in the generator and catalogs together. Missing UI translations fail validation instead of silently publishing an English interface under another language label.
- 主合集数据为 `content/source-cases.json`，外站数据为 `external-sites/source-cases.json`，完整提示词为 `content/prompts.json`。外站目录单独按来源网站展示，中英文详情页生成到 `external-sites/cases/`。新案例沿用已说明的英文内容回退，不要求先补齐另外十四种语言的案例正文。
- Do not translate or reconstruct undisclosed original prompts. Do not relabel a creator claim as independent verification.
- `scripts/presentation.py` 生成本地语言标签、兼容旧链接的导航徽章和多语言素材占位图。首页身份区使用与 YouMind 相同类型的五枚紧凑徽章：Awesome、实时 Stars、MIT、真实校验工作流状态、PRs welcome。
- Star 数量通过 Shields.io 读取本仓库；CI 状态来自本仓库 `validate.yml` 的默认分支徽章。两者均依赖外部图片服务，不在仓库中缓存或手写状态。MIT 徽章链接实际许可证，其适用范围仍为代码和原创文档等；第三方内容遵守各自条款。

界面翻译按英文原文作键维护，缺译会报错；案例新增则走明确的英文回退，不影响每小时收集。首页顺序为标题、仓库徽章、引用式简介、引用式版权声明，再以分隔线连接语言导航。版权入口打开实际存在的 `report-problem.yml` 问题表单。语言标签与占位图从代码本地生成，案例素材继续沿用独立来源和使用条件。

首页 H1 使用 `Awesome {model} Prompts` 翻译键，模型名由配置填入，各语言分别表达“提示词合集”；英文仍为 `Awesome GPT Image 2.6 Prompts`，简体中文为 `GPT Image 2.6 提示词大全`。网页图库标题、截图说明、CTA 和五行功能对照也统一通过 16 语目录生成，当前共用官网英文首页的真实截图。

## Build and verify / 构建与验证

```bash
python3 scripts/build_readme.py
python3 scripts/validate.py
python3 scripts/build_readme.py --check
python3 -m unittest discover -s tests -v
```

The checks cover all locale files, unique paths, all 16 language links, one current-language badge, stable section anchors, existing English/Chinese detail routes, local SVG safety and source-content fallback. See [attribution](ATTRIBUTION.md) for the YouMind layout reference and the scope of each license.
