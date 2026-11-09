# Contributing / 贡献指南

Thanks for helping build this collection. A useful entry includes the actual prompt, a preview or original-source link, the model information that is known, and a clear source credit.

欢迎补充案例。请保留真实提示词、预览图或原帖链接、已知的模型信息与来源署名。

## Source-linked case or complete prompt? / 来源案例还是完整提示词？

来源案例按[维护指南](docs/SOURCE_CASES.md)登记。官方、社媒与论坛、内容发布社区及 GitHub 示例写入 `content/source-cases.json`；其他独立网站写入 `external-sites/source-cases.json`，素材和详情页集中存入[外站素材目录](external-sites/README.md)，不加入主 README 分类和统计。下方完整提示词流程仍使用 `content/prompts.json`。

主合集 README 直接展示图片、提示词和底部署名。已核实的来源原文填写在 `prompt.entries`，每段保留双语标题、原始文本和准确链接；多轮编辑分段保存，不合并成单次指令。不公开或待核验的提示词只标状态。MP4 的首帧预览通过 `python3 scripts/build_video_previews.py` 生成，随后重新生成 README；具体字段与命令见维护指南。

原提示词也可保存为 `cases/<id>/prompt.txt`，并在对应的 `prompt.entries` 条目填写 `path`。文本文件须与 `text` 字段完全一致，末尾增加一个换行；README 和详情页会展示下载链接。X 动图的原始 MP4 与转码 GIF 展示副本分别保存并注明，不把转码副本计为新的案例。

已核实所查来源未提供公开原始提示词，或提示词公开状态尚未检查、无法确认的作品也可收录，但必须独立核对模型证据与来源，并如实区分提示词状态，不伪造原始提示词。

## Suggest a source case / 推荐来源案例

Use the [case suggestion form](https://github.com/RaphaelAI-OpenLab/awesome-gpt-image-2-6/issues/new?template=submit-case.yml) for examples with or without a public prompt. Keep missing prompts explicit and include source/model evidence.

有无公开提示词的案例均可通过案例表单提交，请提供准确原作链接与模型依据。

## Translations / 翻译

The README interface supports 16 languages; case details are currently English and Simplified Chinese. Follow the [language guide](docs/LANGUAGES.md) to improve UI translations without changing original prompts or source claims.

README 界面支持 16 种语言，完整案例详情目前为英文与简体中文。请在翻译目录中维护界面文案，不改写原始提示词或来源陈述。

## Add a complete prompt / 添加完整提示词

1. Copy the complete object in [templates/prompt.json](templates/prompt.json) into the array in [content/prompts.json](content/prompts.json).
2. Keep `status` as `draft` while collecting the missing fields. Drafts are omitted from generated pages, but the JSON itself is visible in a public repository.
3. Add a unique `id`, an English title, the original prompt, a category, and the collection date. A Chinese title is welcome; it falls back to English when empty.
4. Put preview files in `assets/examples/<id>/` and reference images in `assets/references/<id>/`. Displayed images, GIFs and SVGs must be local files, not external hotlinks.
5. Keep the source URL and author. Record image/prompt reuse terms and attribution. If you are only linking to the original image, choose `rights.preview: "link-only"` and leave `preview.path` empty.
6. Set `verification.status` to `source-only` unless you have actually reproduced the result. For a test, record the date, execution platform, and relevant limitations.
7. Switch to `published` when the record is complete, then regenerate and validate.

```bash
python3 scripts/build_readme.py
python3 scripts/validate.py
python3 scripts/build_readme.py --check
```

The generated README and case pages should be committed with the dataset and assets. Do not edit generated files directly.

详细中文操作见 [填充指南](docs/FILLING_GUIDE.zh-CN.md)。

## Attribution / 来源

- Use a direct link to the original post, not a search-results URL.
- Keep the original prompt text. If you adapt it, use `source.provenance: "adapted"` and explain what changed.
- A source saying “GPT Image 2.6” does not establish the Sunburst/Flare variant. Leave the variant `unspecified` if it is unknown.
- Attributing a creator does not automatically grant a license to their image. Use the record's rights fields to distinguish attribution, permission, licensing, and link-only entries.
- Never label a sourced result as our own test without running it.

## Reporting a problem / 报告问题

Use a repository issue to report a broken link, incorrect attribution, model mismatch, or a reproducibility problem. Include the entry ID and the correction or evidence you found.

维护者收到问题后，应修改原始数据并重新生成页面。来源有争议的记录可先改回 `draft`；这会移除公开展示页中的卡片，但不会抹除 Git 历史。

## Scope / 范围

This repository organizes examples and their metadata. It does not call a model API, collect API keys, or make generation requests.

仓库记录案例与相关信息；生成入口只在已配置、实际验证过的逐条链接存在时展示。
