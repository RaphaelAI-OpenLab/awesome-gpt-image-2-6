# Contributing / 贡献指南

Thanks for helping build this collection. A useful entry includes the actual prompt, a preview or original-source link, the model information that is known, and a clear source credit.

欢迎补充案例。请保留真实提示词、预览图或原帖链接、已知的模型信息与来源署名。

## Source-linked case or complete prompt? / 来源案例还是完整提示词？

Use [the source-case guide](docs/SOURCE_CASES.md) for works with prompts linked at the source or no public prompt. Edit `content/source-cases.json`; all published records appear in both README files and internal detail pages. The instructions below apply to complete prompt records in `content/prompts.json`.

没有公开提示词的作品也可收录，但必须明确记录模型证据、来源和缺失状态，不伪造原始提示词。

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
