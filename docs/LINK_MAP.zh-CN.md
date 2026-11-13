# 网站链接位置图

静态网站入口集中在 [site.config.json](../site.config.json)，逐条来源案例集中在 [content/source-cases.json](../content/source-cases.json)，完整提示词入口在 [content/prompts.json](../content/prompts.json)。生成器把入口写入中英文 README 和可选案例页；不需要在多个语言文件里手工替换 URL。

README 的案例详情链接进入仓库内 `cases/<id>/README*.md`。网页图库区展示 GPT Image 2.6 提示词图库的真实截图，截图与“浏览 Raphael GPT Image 2.6 提示词图库”主按钮打开 `https://raphael.app/gpt-image-2-6-prompts`。分类导航使用网站的“全部”及 8 个分类标签，显示网站数量并打开对应语言的分类页。

## 位置与开关

| 位置 | 面向用户的文案或形式 | URL 来源 | 何时显示 | `utm_content` |
| --- | --- | --- | --- | --- |
| 顶栏推广位 | 可替换的活动/新仓库文字，可选横幅图 | `cross_promo.url` | `enabled=true` 且文案、URL 已填 | `cross_promo`；外部 GitHub 链接不加 UTM |
| Hero 封面图 | 点击整个封面进入品牌网站 | `brand.home_url` | 始终显示 | `hero` |
| 网页图库预览图 | GPT Image 2.6 提示词图库真实截图，可点击 | `assets/website/gpt-image-2-6-prompts-20261113.jpg`；链接取 `brand.gallery_url` | 始终显示 | `gallery_preview` |
| 首屏主入口 | 浏览 Raphael GPT Image 2.6 提示词图库 | `brand.gallery_url` 或回退到 `brand.home_url` | 始终显示，按 README 语言翻译 | `top_cta` |
| 仓库案例入口 | 浏览仓库内全部案例 | `#all-cases` | 功能对照表后显示 | 本地不加 UTM |
| 模型使用入口 | 查看当前 GPT Image 2.6 选项 | `brand.model_page_url` | 模型可用状态与验证日期已确认 | `model_entry` |
| 分类导航 | 全部和 8 个网站分类标签，均显示数量 | `brand.gallery_url`、`categories[].website_url`；标签顺序和数量取 `content/web-gallery.json` | 始终显示；链接使用对应语言的网站路径 | `category_all`、`category_<id>` |
| 案例详情入口 | 在 Raphael 查看案例详情 | `links.case_detail_url` | 该条真实详情页存在 | `case_detail_<案例id>` |
| README 案例底部入口 | 👉 立即尝试 → | `brand.gallery_url` | 每个正文案例与精选案例末尾显示；统一打开图库 | `case_gallery_<案例id>` |
| 案例生成入口 | 在 Raphael 使用这条提示词 | `links.generate_url` | 真实深链、验证日期与模型可用状态齐全 | `case_<案例id>` |
| 来源案例列表 | 每条内部详情页 | `content/source-cases.json` 的 ID | `status=published` 时 | 本地不加 UTM |
| 页脚品牌入口 | 访问 Raphael | `brand.home_url` | 始终显示 | `footer` |
| GitHub 右侧 About 的 Website | 网站 URL | 从合集 URL 或首页 URL 生成后，手工填仓库 Settings | 真实远程仓库创建后 | 建议用 `about` |

README 结构由 `scripts/homepage.py` 统一生成，16 种语言共用布局。分类外链按已核对的网页语言路径映射：简体中文为 `/zh/`、繁体中文为 `/zh-Hant/`；西班牙语两版共用 `/es/`，葡萄牙语两版共用 `/pt/`，其余使用对应语言路径，英文不加前缀。品牌外链同时通过 `utm_term` 区分 README 语言，来源与 GitHub 内部链接不加追踪参数。

网页图库区按“标题 → 居中截图 → 主 CTA → 功能对照 → 仓库案例入口”排列。网站分类标签的数量来自 2026-11-13 的实际页面快照，总数为 130；不使用仓库案例数量替代网站数量。修改数量时同步更新 `content/web-gallery.json` 的核对日期与来源。

## 当前真实链接示例

封面入口（英文）：

```text
https://raphael.app/?utm_source=github&utm_medium=repository&utm_campaign=gpt_image_2_6_launch&utm_content=hero&utm_term=en
```

页脚入口（中文）：

```text
https://raphael.app/?utm_source=github&utm_medium=repository&utm_campaign=gpt_image_2_6_launch&utm_content=footer&utm_term=zh-CN
```

`utm_source`、`utm_medium`、`utm_campaign` 可在配置中修改。`utm_content` 由位置决定，`utm_term` 由页面语言决定。原 URL 的功能查询参数与锚点保持保留；已有同名 UTM 会被替换，避免重复。

UTM 是这份框架新增的归因设计，不是对 YouMind 历史实现的描述。它只是在 URL 上记录来源信息；网站还需要自己的统计系统读取，仓库本身不会自动知道点击量或生成转化。

## 更新网站入口与分类数量

1. 核对 `brand.gallery_url` 和 `categories[].website_url` 的实际页面。
2. 更新 `content/web-gallery.json` 中的分类顺序、标签、数量、来源与核对日期。
3. 网站版面变化时，重新截图并同步生成器和校验器引用。
4. 运行生成器和验证器，检查全部语言版本。

逐条案例的独立网页仍由 `links.case_detail_url` 配置。生成深链须在核对模型入口、`model_available` 和 `generate_url_verified_at` 后单独启用。

## 后续新模型怎样借用旧仓库流量

`cross_promo` 是预留的顶栏推广位，可以换成下一代模型合集、季节专题或另一个仓库。开启时填真实文案与地址，结束后关闭或替换。支持可选 `image_path`，但当前没有任何活动在展示。

如果目标是品牌域名上的网页，会添加 `cross_promo` 归因参数；如果是另一个 GitHub 仓库或其他域名，则保留原始地址。

## GitHub About 的 Website 地址

GitHub 仓库右侧的 About 由平台保存，不能仅靠 README 文件设置。创建真实仓库后，可在根目录运行以下命令取得建议 URL，再粘到 About 的 Website：

```bash
python3 - <<'PY'
import sys
sys.path.insert(0, 'scripts')
from common import load_data, tracked_url
config, _ = load_data()
url = config['brand']['gallery_url'] or config['brand']['home_url']
print(tracked_url(url, 'about', 'en', config))
PY
```

不要把 GitHub 的 Stars、Issues、原作者来源、官方模型文档链接替换成品牌跳转。它们提供的价值分别是关注、协作和证据。
