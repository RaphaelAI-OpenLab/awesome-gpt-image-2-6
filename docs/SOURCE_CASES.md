# Source-linked cases and local media / 来源案例与本地素材

[English README](../README.md) · [中文 README](../README.zh-CN.md) · [贡献指南](../CONTRIBUTING.md)

## Data sources / 数据源

### 收录范围

来源案例仅收录官方、社媒与论坛、内容发布社区及 GitHub 示例，统一写入 `content/source-cases.json`，中英文详情页位于 `cases/<id>/README*.md`。

生成器维护案例索引与详情页；校验器检查数据、素材、重复 ID、本地链接和直接来源范围。其他独立网站的原始案例、原图及专属报告保留在同级 `gpt-image-2-6-external-materials-20261112/`，不搬回来源案例集。

使用外站公开的完整提示词独立生成的新图，可作为实测配方写入 `content/prompts.json`。保留准确来源与作者，原文照用时标记 `source.provenance: collected`，改写时标记 `adapted` 并说明修改。只有真正执行并留有模型、参数和结果证据后才标记 `verification.status: tested`；第三方提示词的署名不等于授权，新生成图片也不继承来源原图的权利状态。生成实验和完整任务记录先存放在同级 `raphael-prompt-studio/`，正式收录时只复制发布所需的新图、配方和脱敏生成证据。

完整配方展示在 README 的“完整提示词”区，并生成中英文详情页；有已发布配方时，网页图库主按钮下方提供该区的直接入口。`presentation.featured_case_ids` 仍只配置来源案例，不填写完整配方 ID。

### 网站标签导航与内部案例分类

首页“按分类浏览”展示 [Raphael GPT Image 2.6 图库](https://raphael.app/gpt-image-2-6-prompts) 的“全部”和八个分类标签，并直接链接对应的网站页面。标签顺序、中英文名称及数量快照由 `content/web-gallery.json` 维护；2026-11-13 核对时总计为 130。分类可能交叉，分类数量之和不要求等于总计，也不代表本仓库案例数量。更新时重新查看网站，连同 `verified_at` 一起更新快照。

网站分类地址读取 `site.config.json` 的 `categories[].website_url`，“全部”读取 `brand.gallery_url`。生成器根据 README 语言添加已核验的网站语言前缀，并添加归因参数；新增或更名标签需同步维护 16 种语言的界面译文。

`content/browse.json` 继续保存内部的使用场景、风格、主题三组分类，供案例维护和本地制作工具读取，不再生成首页分类导航。每个子类通过 `case_ids` 关联已发布案例；新增案例仍至少选择一个使用场景，风格与主题依据作品、原文提示词或来源说明填写。同一案例可属于多个子类，不按文件格式推定风格。原有 `category` 字段继续用于 README 正文分组。

精选由 `site.config.json` 中 `presentation.featured_case_ids` 按稳定案例 ID 指定顺序，`featured_limit` 控制展示上限；同步维护案例数据中的 `featured` 标记。精选保留全部案例中的编号，按“素材图片 → 原始提示词 → 作者与来源”完整展开，图片与 GIF 可混合排列；未公开提示词继续明确标记，静态海报不冒充 GIF。

- `content/source-cases.json`: source-linked cases, including works without public prompts. Both languages are required. The schema is `content/source-cases.schema.json`.
- `content/prompts.json`: complete original prompts and reproducibility metadata. This dataset keeps its existing schema. Do not copy a source-case record into it without the actual prompt and appropriate reuse terms.
- `docs/CASE_GALLERY.md`: dated research record, including media reports and unresolved leads. It is historical context, not the live case count.
- 待核线索见 [模型或来源待核线索](PENDING_MODEL_LEADS_2026-11-08.md) 与 [其他存量待核线索](PENDING_REMAINING_LEADS_2026-11-09.md)。两份文档仅保留收录范围内的来源记录，不代表已确认使用 2.6，也不计入已发布案例。
- 不直接编辑自动生成的 README 或案例详情页。已发布案例展示在主 README 分类中，并保留中英文详情页。

### README 图片与提示词展示

主 README 的 16 个语言版本按用途逐条展开主合集案例，顺序为结果图片、原始提示词、作者和来源，最后显示粗体的“👉 立即尝试 →”入口。正文和精选案例的该入口统一打开 `brand.gallery_url` 指定的 Raphael 提示词图库，不预填案例提示词；按案例 ID 与 README 语言添加归因参数。正文分类与精选保留页内案例入口，来源详情链接保留完整模型依据和素材使用条件；顶部的网站标签导航进入 Raphael 图库。参考输入单独折叠展示，不混入结果图片；未入库的图片保留原始链接和缺失说明。

已核对的来源提示词写入案例的 `prompt.entries`，每段包含双语 `title`、保留原文的 `text` 和准确的 `url`；多轮编辑按执行顺序分段，成组 GIF 按输出分别记录。可选的双语 `prompt.note` 用于说明拼接规则、输入缺失或从源图摘录的情况。只有 `source-only` 状态允许携带原文，不把图像描述或推测补写为原始提示词。`content/prompts.json` 继续用于带完整复现元数据的独立配方，摘录原文不等于已独立复现。

仓库统计中的“完整提示词”按实际展示的原文段数计数，“来源公开原始提示词”按有公开原文的案例数计数；同一案例可包含多段原文。网站标签上的数字单独来自上述图库快照。来源素材文件数不包含为 README 派生的视频首帧。

MP4 在 README 中使用独立的首帧 JPEG 作为可点击预览，明确标注为静态首帧，点击打开来源视频。首帧存放在 `assets/readme-previews/<案例 ID>/`，不覆盖原件，也不冒充来源原始 GIF。新增或替换主合集 MP4 后运行：

```bash
python3 scripts/build_video_previews.py
python3 scripts/build_readme.py
python3 scripts/validate.py
```

`build_video_previews.py` 需要本机安装 `ffmpeg`。现有首帧随仓库保存；常规 README 生成与 CI 校验无需调用 `ffmpeg`。

Prompt availability is independent of model evidence, attribution and media reuse eligibility:

- `source-only`: the public original prompt has been verified; `prompt.url` links to it. Verified original text can be stored in `prompt.entries` for inline display.
- `not-public`: the original prompt is confirmed not publicly provided in the reviewed source; `prompt.url` is `null`. Directly observed absence is sufficient; an explicit creator declaration is not required. This describes the reviewed source, not the creator's intent or availability elsewhere.
- `unverified`: public availability of the original prompt was not checked or could not be established; `prompt.url` is `null`. Keep the exact original post in `source.url`, not in `prompt.url`. This status makes no claim about public availability and does not count toward original prompts available at source.

来源案例可以没有公开提示词。`prompt.status` 使用 `source-only`（已核实公开的真实原文）、`not-public`（已核实所查来源未提供公开原始提示词）或 `unverified`（提示词公开状态待核验，尚未检查或无法确认）；后两者的 `prompt.url` 均为 `null`，准确原帖链接保留在 `source.url`。`not-public` 可依据直接检查所查来源确认，不要求作者明确声明，也不推断作者意图或其他来源的公开情况。`unverified` 不断言提示词是否公开，也不计入来源公开原始提示词数量。不要填写猜测或自行改写的假原文。

An unverified prompt does not relax any publication requirement for the case's exact source, creator, work-specific model evidence or media provenance and reuse status. Leads with insufficient model attribution remain outside the published case count.

提示词待核验不放宽案例的准确来源、作者、该作品模型依据、素材来源与使用状态要求。媒体报道或模型归因不充分的线索继续放在检索记录，不混入已核对来源的案例总数。

## Add a source case / 添加来源案例

1. 复制同类记录或 [来源案例模板](../templates/source-case.json)，写入 `content/source-cases.json`。ID 必须在来源案例及完整提示词数据中保持唯一；证据不完整时保留 `status: draft`，草稿只存在于公开 JSON，不生成展示页。
2. Record the exact source URL, creator and model evidence for that specific work. A page mentioning 2.6 does not prove every image used it. Use `variants: ["unspecified"]` when the variant is unknown.
3. Add English and Chinese titles, notes and evidence, an existing category, and ISO collection/check dates. Community creator claims use `source.type: community`, not independent verification.
4. For a verified public original prompt, set `prompt.status: source-only` and its exact HTTPS URL. Use `not-public` when the original prompt is confirmed not publicly provided in the reviewed source, including directly observed absence. Use `unverified` when public availability was not checked or could not be established. Both latter statuses require `url: null`; always retain the exact original post in `source.url`.
5. Add original media links when known. Unknown source URLs are not fabricated. Archive normally accessible public examples with truthful provenance and use status. Use `rights.status: link-only`, `path: null` for explicit redistribution restrictions, access failures or unresolved files, with the precise reason.
6. Run the commands below, inspect the generated pages, then commit the data, code if changed, local assets and generated pages together. Read the latest remote head before publishing; never force-push over newer work.

## Store media with provenance / 收录素材与来源

素材必须记录来源与真实使用状态。公开可见、注明来源、AI 生成、出现在官方网页，均不自动等于获得转载许可。可正常获取且未发现明确禁止的公开案例可原样存档，使用 `source-attributed` 明确标注未找到转载许可证；这不是开放许可或法律结论。首页版权声明不自动赋予许可。明确限制必须遵守，不绕过访问控制。

- 输出存放于 `assets/examples/<id>/`，参考输入存放于 `assets/references/<id>/`；数据内的 `media.path` 从仓库根目录开始记录。不使用图片、GIF 或 SVG 外链展示。
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
