# Source-linked cases and local media / 来源案例与本地素材

[English README](../README.md) · [中文 README](../README.zh-CN.md) · [贡献指南](../CONTRIBUTING.md)

## Data sources / 数据源

- `content/source-cases.json`: source-linked cases, including works without public prompts. Both languages are required. The schema is `content/source-cases.schema.json`.
- `content/prompts.json`: complete original prompts and reproducibility metadata. This dataset keeps its existing schema. Do not copy a source-case record into it without the actual prompt and appropriate reuse terms.
- `docs/CASE_GALLERY.md`: dated research record, including media reports and unresolved leads. It is historical context, not the live case count.
- Never edit generated README or `cases/<id>/README*.md` files directly. Every published source case appears in both README category lists and has two internal detail pages.

来源案例可以没有公开提示词。`prompt.status` 使用 `source-only`（链接真实原文）或 `not-public`（明确未公开）；不要填写猜测或自行改写的假原文。媒体报道或模型归因不充分的线索继续放在检索记录，不混入已核对来源的案例总数。

## Add a source case / 添加来源案例

1. Copy a structurally similar record from `content/source-cases.json`, or use [templates/source-case.json](../templates/source-case.json). Keep a unique stable `id` across both datasets. Keep `status: draft` until the required evidence is complete; drafts remain public in JSON but are not displayed.
2. Record the exact source URL, creator and model evidence for that specific work. A page mentioning 2.6 does not prove every image used it. Use `variants: ["unspecified"]` when the variant is unknown.
3. Add English and Chinese titles, notes and evidence, an existing category, and ISO collection/check dates. Community creator claims use `source.type: community`, not independent verification.
4. For a public original prompt, set `prompt.status: source-only` and its exact HTTPS URL. Otherwise use `not-public` with `url: null`.
5. Add original media links when known. Unknown source URLs are not fabricated. Archive normally accessible public examples with truthful provenance and use status. Use `rights.status: link-only`, `path: null` for explicit redistribution restrictions, access failures or unresolved files, with the precise reason.
6. Run the commands below, inspect the generated pages, then commit the data, code if changed, local assets and generated pages together. Read the latest remote head before publishing; never force-push over newer work.

## Store media with provenance / 收录素材与来源

素材必须记录来源与真实使用状态。公开可见、注明来源、AI 生成、出现在官方网页，均不自动等于获得转载许可。可正常获取且未发现明确禁止的公开案例可原样存档，使用 `source-attributed` 明确标注未找到转载许可证；这不是开放许可或法律结论。首页版权声明不自动赋予许可。明确限制必须遵守，不绕过访问控制。

- Store example files at `assets/examples/<id>/` and required inputs at `assets/references/<id>/`. Do not hotlink image/GIF/SVG displays.
- Each source-case media object records its original `source_url`, local `path`, `kind` (`image`, `gif`, `svg`, `poster`, `video`), bilingual alt text and `rights`. Use `role: reference` for input/reference files in `assets/references/<id>/`, and `role: output` for generated outputs. Local files also require actual `mime_type`, `bytes` and SHA-256 `sha256`; the validator checks bytes, extension and media kind.
- Use `licensed`, `permission` or `original` only when supported. `source-attributed` records a public example archived with its exact original source and an explicit note that a redistribution license was not located; do not present it as permission or an open license. Record `rights.evidence_url` as an exact HTTPS license/permission link, the exact original source for source-attributed media, or a public-safe in-repository evidence file. Include `credit` and bilingual limitations in `note`. Do not upload private email, secrets or personal data as evidence.
- A `link-only` object must not have a local path. Local media must have source/rights evidence, exist at the required path and be at most 10 MiB each. A static poster is not a GIF; label it correctly.
- Keep original-page access separate from media-file access. Optional case `access` metadata records `page_status`, `media_status`, bilingual notes, check date and an internal `report_path`. A direct-media HTTP 403 does not by itself mean the post cannot open. When an ordinary public browser shows the media, use its supported save/download path; stop at actual security or access denials. See the [per-file recheck](MEDIA_ACCESS_2026-11-05.md).
- Use `kind: video` for MP4 animations, including X attachments labelled GIF by the interface. Local MP4 files use a repository download link, not image markup. Prefer a separately recorded local poster for image previews. Never mislabel MP4 as an original GIF. The [2026-11-05 media report](MEDIA_RIGHTS_2026-11-05.md) distinguishes archived media, unknown licensing and actual HTTP 403 failures.
- View image pixels and play GIFs before describing their visual quality. Verify SVGs have no scripts, embedded secrets or external resource dependencies. Do not claim a playback/render check that was not run.
- For complete prompt entries, keep preview/reference files local too and record applicable rights. A third-party preview with permission/licensing must have a `rights.license_url`; attribution alone is insufficient.

已入库素材按记录自动显示，统计从数据源计算。参考输入、静态海报、原始动画和栅格预览须区分；占位图不计入素材数量。HTTP 403 等失败必须记录实际原因，不能写成“作者禁止转载”。补齐文件与来源 / 使用状态后重新生成，无需手改 README。

## Build and checks / 构建与检查

```bash
python3 scripts/build_readme.py
python3 scripts/validate.py
python3 scripts/build_readme.py --check
python3 -m unittest discover -s tests -v
```

The build is deterministic. `--check` detects edited/missing generated files and stale generated case pages. Validation checks schemas, IDs, bilingual text, source links, local routes, rights metadata and asset paths. CI runs these checks on pushes and pull requests.

构建没有调用生图 API，也不创建网站或收费服务。外部图库、一键生成、关联活动与 Star 历史图尚未配置时显示明确占位文字，不使用虚构 URL。
