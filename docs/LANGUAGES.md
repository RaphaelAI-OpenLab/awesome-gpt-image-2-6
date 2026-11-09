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
- `scripts/presentation.py` generates language badges, repository navigation badges and localized media placeholders. They use original local SVG artwork, with no remote image dependencies.
- CI and Star badges are navigation links, **not cached pass/fail states or star counts**. Open the actual GitHub workflow or repository to see live values. The Star History link uses the current canonical repository; no third-party chart image is embedded.

界面翻译按英文原文作键维护，缺译会报错；案例新增则走明确的英文回退，不影响每小时收集。徽章不伪装实时 CI 成绩或 Star 数量。所有装饰性标签与占位图都从代码本地生成，案例素材继续沿用独立来源和使用条件。

## Build and verify / 构建与验证

```bash
python3 scripts/build_readme.py
python3 scripts/validate.py
python3 scripts/build_readme.py --check
python3 -m unittest discover -s tests -v
```

The checks cover all locale files, unique paths, all 16 language links, one current-language badge, stable section anchors, existing English/Chinese detail routes, local SVG safety and source-content fallback. See [attribution](ATTRIBUTION.md) for the YouMind layout reference and the scope of each license.
