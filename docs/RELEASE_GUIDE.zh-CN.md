# 仓库发布与维护

## 当前状态

仓库已有结构化来源案例、双语 README 与内部详情页；数量以 README 自动统计为准。完整提示词数据与来源案例分开统计。GitHub owner 已配置为 `netlogs`；网站模型与合集入口尚未核验时显示占位，不假定已上线。Raphael 主页链接与案例入口明确区分。

## 一次性仓库设置

| 项目 | 建议值或操作 |
| --- | --- |
| Repository name | `awesome-gpt-image-2-6` |
| Description | `GPT Image 2.6 prompts, visual examples, and original sources. An open collection by Raphael.` |
| Topics | `gpt-image-2-6`, `image-generation`, `prompts`, `prompt-library`, `openai`, `design`, `raphael` |
| Default branch | `main` |
| About / Website | 按 [链接位置图](LINK_MAP.zh-CN.md) 生成 URL 后填写 |
| Social preview | 第一批真实案例备好后，制作准确展示这些案例的预览图再上传 |

将真实 GitHub 用户/组织名填入 `site.config.json` 的 `project.repository_owner`。如果改仓库名，同步改 `repository_slug`。

## 先放框架

在本地运行以下命令，可以确认框架自身完整：

```bash
python3 scripts/build_readme.py
python3 scripts/validate.py
python3 scripts/build_readme.py --check
```

保持 `content/prompts.json` 为空是支持的状态。不要为了让页面显得丰富而填虚假数量、伪造模型输出，或把占位图当作已收录案例。

## 再开始内容推广

第一批真实内容准备完成后：

1. 按 [填充指南](FILLING_GUIDE.zh-CN.md) 补齐记录，并设置为 `published`。
2. 检查中英文 README、分类链接、图片、原帖署名和每条可用入口。
3. 运行发布前检查：

```bash
python3 scripts/validate.py --release
python3 scripts/build_readme.py --check
```

`--release` 会指出没有公开案例、未设置真实 GitHub owner、未记录内容使用条件等尚未完成项。没有确认网站支持该模型时，会提醒保留通用主页文案；它不会强迫你在合集仓库上线前改造网站。

选择实际存在的页面作为推广承接地址。仓库、网站合集与直接生成入口是不同的目标，外部帖文应与对应入口的真实体验一致。

## GitHub Actions

[validate.yml](../.github/workflows/validate.yml) 在 push、pull request 和手动触发时运行以下检查：

- 数据结构与字段完整性。
- 预览图、参考图和仓库内链接存在。
- 生成的 README/案例页与当前数据一致。

工作流仅申请仓库内容读取权限，没有发布、发帖或模型调用步骤，不需要 API key。

## 日常改动

| 改动 | 修改位置 |
| --- | --- |
| 添加或撤下案例 | `content/prompts.json`；撤下用 `draft` 后重新生成 |
| 网站合集正式上线 | `brand.gallery_url` |
| 某个分类页上线 | 对应 `categories[].website_url` |
| 提供模型的真实使用入口 | `brand.model_page_url`、`model_available`、验证日期 |
| 某条提示词能通过深链打开 | 该条 `links.generate_url` 与验证日期 |
| 顶部切换新专题/新模型 | `cross_promo` |
| 修改渠道归因活动名 | `tracking.utm_campaign` |
| 调整首页精选条数 | `presentation.featured_limit` |

每次改动后重新生成并验证，再把源数据与生成文件一起提交。

## 内容提交时的简短检查

- 实际案例数与 README 自动统计一致。
- 来源、模型版本与实测状态写的是已知信息。
- 有参考图要求时，材料和步骤足够让别人理解输入。
- 网站 URL 已真实打开核对；自动校验只检查格式，不会证明外部网页功能可用。
- 原始提示词没有被中英文页面的翻译流程改写。

历史研究与对外推广时间安排由这次任务的单独报告交付，不混进公共 README。
