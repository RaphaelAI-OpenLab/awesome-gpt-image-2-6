# 填充指南

当前来源案例由 `content/source-cases.json` 维护，已在双语 README 中展示并链接仓库内部详情页；完整提示词由 `content/prompts.json` 单独维护。首页中标明占位的图片是原创示意，不是模型输出。最新数量请以 README 自动统计为准。

无公开提示词的作品和本地素材管理，先看[案例与素材维护指南](SOURCE_CASES.md)。本文其余步骤主要适用于完整提示词记录。

## 1. 文件分别负责什么

| 文件或目录 | 你需要做什么 |
| --- | --- |
| [site.config.json](../site.config.json) | 配置品牌、网站地址、GitHub owner、分类、推广位与归因参数 |
| [content/prompts.json](../content/prompts.json) | 所有真实案例的唯一数据源；现在是空数组 |
| [templates/prompt.json](../templates/prompt.json) | 完整空白记录；复制到数据数组再填写 |
| [content/schema.json](../content/schema.json) | 字段、类型与可选值说明 |
| `assets/examples/<案例id>/` | 存放已获相应使用条件的效果图、预览 GIF 或 SVG |
| `assets/references/<案例id>/` | 存放用户复现时需要的参考图 |
| `README.md`、`README.<locale>.md` | 自动生成的 16 语界面首页，不直接修改；详情见 [多语言维护](LANGUAGES.md) |
| `cases/<案例id>/README.md`、`README.zh-CN.md` | 发布案例后自动生成的中英文独立详情页 |
| [scripts/build_readme.py](../scripts/build_readme.py) | 生成页面；改布局时才需要改脚本 |
| [scripts/validate.py](../scripts/validate.py) | 检查数据、素材路径、本地链接与发布准备情况 |

运行环境为 Python 3.10 或更高版本，无第三方依赖。

## 2. 先配置固定信息

打开 `site.config.json`：

- `project.repository_owner`：填真实 GitHub 用户或组织名。留空时不会生成虚假的 Star/Issue 仓库链接。
- `brand.home_url`：当前为真实的 `https://raphael.app/`。
- `brand.gallery_url`：GPT Image 2.6 合集网页真实上线后，再填写它的完整 URL。没有就保持 `null`。
- `brand.model_page_url`：真实的模型使用页面，没有就保持 `null`。
- `brand.model_available`：确认网站实际可以使用该模型后再改为 `true`，并填 `model_support_verified_at`。
- `categories[].website_url`：分类网页真正存在时填写；现在全部是 `null`，导航指向本仓库内部。
- `cross_promo`：给后续新模型、活动或新仓库留的顶栏位置。默认关闭；详见 [网站链接位置图](LINK_MAP.zh-CN.md)。

修改模型或品牌以复用到下一代仓库时，也要同步调整 `assets/header.svg` 中的标题、版本和品牌署名字样。其余品牌链接由配置生成。

## 3. 添加第一条真实记录

把 `templates/prompt.json` 的整个对象复制进 `content/prompts.json` 的数组。多条记录之间用逗号隔开。初始 `status` 为 `draft`，可以分次填写。

**`draft` 只表示不出现在自动生成的展示页里。仓库公开后，JSON 和 Git 历史仍然可见，不要把私密素材或未公开客户信息当作隐藏草稿存进去。**

| 字段 | 如何填 |
| --- | --- |
| `id` | 稳定且唯一的小写短横线 ID；以后网址和图片目录都使用它 |
| `status` | 未完成用 `draft`；准备展示用 `published` |
| `title.en`、`title.zh-CN` | 英文标题必填；中文可后补，暂时为空会使用英文 |
| `summary` | 简短说明这条案例能做什么，不夸大未测试的能力 |
| `category` | 从下方 8 个分类 ID 中选择一个 |
| `tags` | 用来进一步标记用途，允许为空 |
| `prompt_language` | 原始提示词的语言，如 `en` 或 `zh-CN` |
| `prompt` | 完整原始提示词；不要把翻译版本冒充原文 |
| `preview.path`、`preview.alt` | 效果图相对路径或 HTTPS URL，以及图片说明 |
| `reference_images` | 参考图的 `path` 与中英文 `description`；没有就留空数组 |
| `model`、`workflow` | 已知模型、设置、输出形式与操作步骤，见下一节 |
| `source` | 原始帖子、作者、平台、发布日期，以及原创/收集/改写状态 |
| `verification` | 原帖案例与自己的实测分开记录 |
| `rights` | 提示词与图片的使用条件、署名、可选授权说明链接 |
| `added_at` | 本仓库收录日期，格式 `YYYY-MM-DD`，不是随意复制原帖日期 |
| `featured` | `true` 表示优先进入首页效果网格；默认最多 6 条 |
| `links` | 可选网站详情页与已验证生成深链；没有就保留 `null` |
| `notes` | 失败条件、结果限制、人工处理说明等补充信息 |

### 分类 ID

| ID | 用途 |
| --- | --- |
| `brand-products` | 品牌与商品 |
| `posters-typography` | 海报与文字排版 |
| `infographics` | 信息图 |
| `interiors-architecture` | 室内与建筑 |
| `characters-consistency` | 角色与一致性 |
| `markup-edits` | 标注与局部编辑 |
| `svg-design-assets` | SVG 与设计素材 |
| `gif-animation` | GIF 与动画 |

这些只是内容容器，并不表示仓库已经有案例。

## 4. 模型、参数、来源与实测

### 模型信息

`model.family` 使用 `GPT Image 2.6`。官方 API 型号目前为：

- Sunburst：`gpt-image-2.6-sunburst`
- Flare：`gpt-image-2.6-flare`

只知道作者写了 GPT Image 2.6，而不知道具体版本时，保留 `variant: "unspecified"` 和 `api_model_id: null`。不要从图片观感猜型号。

`workflow.task_type` 可选 `generation`、`editing`、`vector`、`animation`。

`workflow.parameters` 留有 `size`、`quality`、`complexity`、`output_format`。不知道的值留 `null`，不要把默认值当作作者实际使用的值。`workflow.extra_parameters` 用来保留其他已知设置，例如背景或输入保真设置；它只是案例元数据，不会被脚本发送给模型。

`quality` 与 `complexity` 是两个不同字段；后者支持 `low`、`medium`、`high`。GIF/SVG 与参考图也有独立位置，避免未来补数据时只能塞进一段文字。官方能力说明见 [OpenAI 发布说明](https://openai.com/index/introducing-images-2-6/) 与 [图像文档](https://developers.openai.com/api/docs/guides/image-generation)。

### 原帖记录

`source.provenance` 有三种：

- `original`：自己制作的案例。
- `collected`：收集他人公开案例，保留原始帖子与作者。
- `adapted`：基于原提示词修改，保留来源并在 `notes` 说明修改。

原帖记录本身不等于复现结果。仅收集时，使用 `verification.status: "source-only"`；页面会显示“来自原帖 · 尚未独立实测”。

### 自己的实测

真正执行后再使用 `verification.status: "tested"`，填写 `tested_at`、`tested_on` 与结果说明。最好写清哪些参数已确认、有没有人工修图、哪些输入会失败。

### 使用条件

`rights.prompt` 可选 `own`、`permission`、`licensed`、`source-attributed`、`unknown`。其中 `source-attributed` 只说明已标明来源，不代表获得了可转授权的许可。

`rights.preview` 可选 `own`、`permission`、`licensed`、`link-only`、`unknown`。如果只提供原帖入口，用 `link-only`，保留 `source.url`，把 `preview.path` 留空；页面就不会嵌入这张图。

MIT 协议仅覆盖本框架的代码、模板和原创说明，不自动覆盖后来收集的第三方内容。

## 5. 网站链接怎么接

每条案例的两个地址各有用途：

| 字段 | 展示给用户的入口 | 何时出现 |
| --- | --- | --- |
| `links.case_detail_url` | 在 Raphael 查看案例详情 | 真实详情页 URL 已填写 |
| `links.generate_url` | 在 Raphael 使用这条提示词 | 已填真实生成深链、`generate_url_verified_at`，且配置确认该模型可用 |

详情页链接不能当作“一键使用”。跳转到通用首页的链接也不能填进 `generate_url` 来制造这个承诺。测试深链时要确认模型、提示词和必要输入能按预期传递。

已有 `id`、`categories` 等功能参数会被保留。脚本只新增或替换本仓库的 UTM 归因参数，不会给作者原帖、官方文档或 GitHub 链接添加这些参数。

## 6. 生成与检查

在仓库根目录运行：

```bash
python3 scripts/build_readme.py
python3 scripts/validate.py
python3 scripts/build_readme.py --check
```

生成器会同步中英文 README、首页效果网格、分类计数、最近收录，以及可选的独立案例页。日期排序按 `added_at`；将条目改回 `draft` 会移除其生成页面。

`presentation.generate_case_pages` 控制独立案例页。关闭后只保留 README 卡片；脚本只删除自己生成且带标记的旧案例页，不处理其他手写文件。

当前空框架应该通过普通验证。`python3 scripts/validate.py --release` 是开始内容推广前的额外检查：由于目前没有案例、GitHub owner 尚未填写，它会按预期返回未就绪。是否已经确认 Raphael 提供 2.6 会单独提示；仅保留通用主页入口时，不要求先开通该模型。

检查完成后，把数据、图片、生成的页面一起提交。后续更换网站入口只需改配置并重新生成。
