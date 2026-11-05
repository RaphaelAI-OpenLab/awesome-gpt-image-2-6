# 网站链接位置图

静态网站入口集中在 [site.config.json](../site.config.json)，逐条案例入口集中在 [content/prompts.json](../content/prompts.json)。生成器把入口写入中英文 README 和可选案例页；不需要在多个语言文件里手工替换 URL。

当前只有真实的 Raphael 首页启用。合集、分类、模型页、案例详情与生成深链都没有编造地址。

## 位置与开关

| 位置 | 面向用户的文案或形式 | URL 来源 | 何时显示 | `utm_content` |
| --- | --- | --- | --- | --- |
| 顶栏推广位 | 可替换的活动/新仓库文字，可选横幅图 | `cross_promo.url` | `enabled=true` 且文案、URL 已填 | `cross_promo`；外部 GitHub 链接不加 UTM |
| Hero 封面图 | 点击整个封面进入品牌网站 | `brand.home_url` | 始终显示 | `hero` |
| 顶部导航 | `Raphael ↗` | `brand.home_url` | 始终显示 | `top_nav` |
| 首屏主按钮 | 有合集时“浏览完整效果合集”；否则“访问 Raphael” | `brand.gallery_url`，缺省用 `home_url` | 始终显示 | `top_cta` |
| 模型使用入口 | 查看当前 GPT Image 2.6 选项 | `brand.model_page_url` | 模型可用状态与验证日期已确认 | `model_entry` |
| 分类导航 | 8 个用途分类名 | 每个分类的 `website_url` | 地址非空时导向网站；否则跳到本仓库分类 | `category_<分类id>` |
| 案例详情入口 | 在 Raphael 查看案例详情 | `links.case_detail_url` | 该条真实详情页存在 | `case_detail_<案例id>` |
| 案例生成入口 | 在 Raphael 使用这条提示词 | `links.generate_url` | 真实深链、验证日期与模型可用状态齐全 | `case_<案例id>` |
| 合集内容底部 | 浏览完整效果合集 | `brand.gallery_url` | 真实合集已上线 | `collection_bottom` |
| 页脚品牌入口 | 访问 Raphael | `brand.home_url` | 始终显示 | `footer` |
| GitHub 右侧 About 的 Website | 网站 URL | 从合集 URL 或首页 URL 生成后，手工填仓库 Settings | 真实远程仓库创建后 | 建议用 `about` |

README 内还保留了 `<!-- SLOT: ... -->` 注释，方便找到各个位置。英文与中文共用同一套布局，语言通过 `utm_term` 区分。

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

## 合集网站上线时改哪些字段

1. 将真实的合集 URL 填入 `brand.gallery_url`。
2. 将真实的分类 URL 逐个填入 `categories[].website_url`。支持原网站需要的查询参数，不猜测路径格式。
3. 每个案例若有独立网页，填 `links.case_detail_url`。
4. 实际支持 GPT Image 2.6 后，再填模型页、确认日期与 `model_available`。
5. 逐条检查生成深链，记录 `generate_url_verified_at` 后再启用。
6. 重新运行生成器和验证器。

只上线合集网页时，完成前 3 项即可。生成入口不必同步开启。

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
