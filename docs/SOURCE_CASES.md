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
5. Add original media links when known. Unknown source URLs are not fabricated. Without reuse permission use `rights.status: link-only`, `path: null`, and a clear rights note. The original work stays accessible through the source.
6. Run the commands below, inspect the generated pages, then commit the data, code if changed, local assets and generated pages together. Read the latest remote head before publishing; never force-push over newer work.

## Store approved media / 收录有依据的素材

素材必须记录来源与真实使用状态。公开可见、注明来源、AI 生成、出现在官方网页，均不自动等于获得转载许可。本轮按用户要求，将可正常获取且未发现明确禁止的少量官方 AI 示例原样存档，使用 `source-attributed` 明确标注未找到转载许可证；这不是开放许可或法律结论。明确限制必须遵守，不绕过访问控制。

- Store example files at `assets/examples/<id>/` and required inputs at `assets/references/<id>/`. Do not hotlink image/GIF/SVG displays.
- Each source-case media object records its original `source_url`, local `path`, `kind` (`image`, `gif`, `svg`, `poster`), bilingual alt text and `rights`.
- Use `licensed`, `permission` or `original` only when supported. `source-attributed` is reserved for a public official example archived with its exact source and an explicit note that a redistribution license was not located; do not present it as permission or extend it to unrelated third-party works. Record `rights.evidence_url` as an exact HTTPS license/permission link, the original official source for source-attributed media, or a public-safe in-repository evidence file. Include `credit` and bilingual limitations in `note`. Do not upload private email, secrets or personal data as evidence.
- A `link-only` object must not have a local path. Local media must have source/rights evidence, exist at the required path and be at most 10 MiB each. A static poster is not a GIF; label it correctly.
- View image pixels and play GIFs before describing their visual quality. Verify SVGs have no scripts, embedded secrets or external resource dependencies. Do not claim a playback/render check that was not run.
- For complete prompt entries, keep preview/reference files local too and record applicable rights. A third-party preview with permission/licensing must have a `rights.license_url`; attribution alone is insufficient.

本轮原样收录 3 个官方文档示例文件（2 个 SVG、1 个 GIF），明确标注未找到转载许可证；其余素材仍链接原作。占位图明确写明“素材暂未入库”，不计入本地原始素材数量。补齐相应素材及来源/使用状态后，页面自动显示，无需手工改 README。

## Build and checks / 构建与检查

```bash
python3 scripts/build_readme.py
python3 scripts/validate.py
python3 scripts/build_readme.py --check
python3 -m unittest discover -s tests -v
```

The build is deterministic. `--check` detects edited/missing generated files and stale generated case pages. Validation checks schemas, IDs, bilingual text, source links, local routes, rights metadata and asset paths. CI runs these checks on pushes and pull requests.

构建没有调用生图 API，也不创建网站或收费服务。外部图库、一键生成、关联活动与 Star 历史图尚未配置时显示明确占位文字，不使用虚构 URL。
