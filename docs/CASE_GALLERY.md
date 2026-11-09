# 案例与原始来源索引 / Source-linked case gallery

[返回中文首页](../README.zh-CN.md) · [English README](../README.md)

本页保留首轮检索记录；主合集数据由 [source-cases.json](../content/source-cases.json) 维护，在[中文 README 分类](../README.zh-CN.md#all-cases)展示；其他独立网站的案例、数据与素材已移入[外站素材目录](../external-sites/README.md)，不计入主合集分类和统计。

本轮核对日期：2026-11-05（UTC）。

**37 组官方案例、2 条社区自报案例、1 条媒体报道线索；另有 8 条待核实链接。** 同一工作流的不同模型输出合并为一组，不按图片张数凑数。这里记录来源证据，不表示整理者已复现，也不等于独立效果评测。

本页与[可复制提示词数据](../content/prompts.json)分开维护。原文已公开的长提示词直接链接到来源；没有提示词的作品明确标注缺失。所有第三方图片、GIF、SVG 均只提供原站链接，不下载、不嵌入、不授予转载许可。来源署名不等于授权。

## 官方文档：28 组工作流

作者与来源：[OpenAI 图像提示词指南](https://developers.openai.com/api/docs/guides/image-prompting)。以下每组均检查了对应输出的 **GPT Image 2.6** 标签，且原文有提示词；表中“双版本”表示该组同时列出 Flare 和 Sunburst。参考图、完整参数与结果请在对应章节查看。

| ID | 案例 | 版本 |
| --- | --- | --- |
| docs-complexity | [纸艺夺冠场景：复杂度比较](https://developers.openai.com/api/docs/guides/image-prompting#compare-complexity) | Sunburst |
| docs-bakery-svg | [面包店 SVG 标志](https://developers.openai.com/api/docs/guides/image-prompting#generate-svg-output) | 双版本 |
| docs-lantern-gif | [提灯猴循环 GIF](https://developers.openai.com/api/docs/guides/image-prompting#generate-a-looping-gif) | Sunburst |
| docs-sailor | [渔船水手写实人像](https://developers.openai.com/api/docs/guides/image-prompting#control-style-and-lighting) | 双版本 |
| docs-coffee-diagram | [咖啡机工作流程图](https://developers.openai.com/api/docs/guides/image-prompting#explain-a-process-visually) | 双版本 |
| docs-streetwear | [街头服饰广告排字](https://developers.openai.com/api/docs/guides/image-prompting#render-exact-text) | 双版本 |
| docs-bakery-raster | [面包店透明位图标志](https://developers.openai.com/api/docs/guides/image-prompting#design-a-reusable-logo) | 双版本 |
| docs-historical-crowd | [1969 年历史人群场景](https://developers.openai.com/api/docs/guides/image-prompting#use-historical-and-real-world-context) | 双版本 |
| docs-pet-comic | [宠物四格漫画](https://developers.openai.com/api/docs/guides/image-prompting#turn-a-story-into-a-comic-strip) | 双版本 |
| docs-market-ui | [农夫市场手机界面](https://developers.openai.com/api/docs/guides/image-prompting#create-an-interface-preview) | 双版本 |
| docs-cell-respiration | [细胞呼吸教学图](https://developers.openai.com/api/docs/guides/image-prompting#create-scientific-and-educational-visuals) | 双版本 |
| docs-pitch-slide | [市场规模演示页](https://developers.openai.com/api/docs/guides/image-prompting#build-slides-diagrams-and-charts) | 双版本 |
| docs-vase-markup | [标注花瓶后局部换色](https://developers.openai.com/api/docs/guides/image-prompting#guide-an-edit-with-markup) | 双版本 |
| docs-spanish-edit | [信息图改为西班牙语](https://developers.openai.com/api/docs/guides/image-prompting#translate-while-preserving-layout) | 双版本 |
| docs-pixel-style | [像素风格迁移](https://developers.openai.com/api/docs/guides/image-prompting#transfer-a-visual-style) | 双版本 |
| docs-outfit | [保留人物身份换装](https://developers.openai.com/api/docs/guides/image-prompting#preserve-identity-and-change-clothing) | 双版本 |
| docs-dog-composite | [跨图合成宠物](https://developers.openai.com/api/docs/guides/image-prompting#combine-references) | 双版本 |
| docs-product-cutout | [商品透明背景抠图](https://developers.openai.com/api/docs/guides/image-prompting#create-a-transparent-product-cutout) | 双版本 |
| docs-sketch-render | [线稿转写实场景](https://developers.openai.com/api/docs/guides/image-prompting#turn-a-drawing-into-a-realistic-image) | 双版本 |
| docs-remove-flower | [移除手持花朵](https://developers.openai.com/api/docs/guides/image-prompting#remove-an-object) | 双版本 |
| docs-person-scene | [人物放入露营逃跑场景](https://developers.openai.com/api/docs/guides/image-prompting#insert-a-person-into-a-scene) | 双版本 |
| docs-billboard | [洗发水公路广告牌](https://developers.openai.com/api/docs/guides/image-prompting#create-the-starting-image) | 双版本 |
| docs-snow-edit | [广告牌场景改为雪夜](https://developers.openai.com/api/docs/guides/image-prompting#change-one-condition) | 双版本 |
| docs-character-start | [建立童书角色](https://developers.openai.com/api/docs/guides/image-prompting#establish-the-character) | 双版本 |
| docs-character-story | [同一角色续写故事](https://developers.openai.com/api/docs/guides/image-prompting#continue-the-story) | 双版本 |
| docs-room-chairs | [室内更换椅子](https://developers.openai.com/api/docs/guides/image-prompting#change-furniture-in-a-room) | 双版本 |
| docs-holiday-card | [怀旧节日贺卡](https://developers.openai.com/api/docs/guides/image-prompting#design-a-holiday-card) | 双版本 |
| docs-toy-package | [玩具飞机包装](https://developers.openai.com/api/docs/guides/image-prompting#design-collectible-merchandise) | 双版本 |

注意：市场规模演示页中的数据与引用是虚构示例。该网页后半段仍有标为 **2.5** 的旧 logo 变体，不在上述收录范围。

补充直达文件：[Flare SVG](https://developers.openai.com/images/platform/guides/image-prompting/field-and-flour-gpt-image-2-6-flare.svg) · [Sunburst SVG](https://developers.openai.com/images/platform/guides/image-prompting/field-and-flour-gpt-image-2-6-sunburst.svg) · [Sunburst 提灯猴 GIF](https://developers.openai.com/images/platform/guides/image-prompting/monkey-lantern-gpt-image-2-6-sunburst.gif)。这些地址来自官方页面链接；本轮文本抓取工具不能播放 GIF 或渲染 SVG，未独立检查逐帧效果。

## 官方发布页：9 组演示

共同来源：[OpenAI 发布页，2026-11-04](https://openai.com/index/introducing-images-2-6/)。以下均由发布页归为 Images 2.6 演示。合作方标签中可展开案例；未明确写出的版本不推测。

| ID | 作者 / 署名 | 案例 | 版本 | 原始提示词 |
| --- | --- | --- | --- | --- |
| launch-openart-down | OpenArt | 股价下跌的办公角色 GIF | 未注明 | 发布页 Prompt 1 可读 |
| launch-openart-up | OpenArt | 股价上涨的办公角色 GIF | 未注明 | 发布页 Prompt 2 可读 |
| launch-owl | OpenAI 发布页 | 猫头鹰草图变动画 | 未注明 | 未公开 |
| launch-town | Town | Monty 打字状态动画 | 未注明 | 未公开 |
| launch-picsart | Picsart | 彩色玻璃鲸鱼 | 未注明 | 未公开 |
| launch-fal | fal | 客厅标注编辑 | Flare | fal 标签可读 |
| launch-sable | Sable | 品牌产品微缩场景 | Sunburst | Sable 标签可读 |
| launch-higgsfield | Higgsfield | 骑士连续换景换装 | 未注明 | Higgsfield 标签可读；需初始图 |
| launch-travel | OpenAI 发布页 | 旅行视觉生成速度对比 | 未注明 | 未公开 |

原站预览入口（静态海报不是 GIF 文件）：
- OpenArt：[下跌版海报](https://images.ctfassets.net/kftzwdyauwt9/2buvg5udbd1nwQv8AFYzpM/1041a34b4048cde3b1f5b93658624a90/images-2-6-openart-market-down-poster.jpg?w=3840&q=50&fm=webp)、[上涨版海报](https://images.ctfassets.net/kftzwdyauwt9/4vIjzvIPc4VGiNVNoIIe1X/cdbffef89e0dc801a57526314deae7ac/images-2-6-openart-market-up-poster.jpg?w=3840&q=50&fm=webp)。
- 猫头鹰：[草图](https://images.ctfassets.net/kftzwdyauwt9/7xC8whl4xN2cOTxQSLMfQ8/60b25185d53ca63f000341f0acbfba7a/owl-sketch-square.png?w=3840&q=90&fm=webp)、[动画海报](https://images.ctfassets.net/kftzwdyauwt9/3htx622jZc5ImLeWZfZhEX/52551971a364017e1d4c0da98b5e334f/owl-animation-poster.jpg?w=3840&q=50&fm=webp)。
- Town：[动画海报](https://images.ctfassets.net/kftzwdyauwt9/56j4cAmTWrRJgTSQEvLQ01/90f1805a4e72b7e2498863da19766c65/town-monty-poster.jpg?w=3840&q=50&fm=webp)。
- Picsart：[鲸鱼图](https://images.ctfassets.net/kftzwdyauwt9/5g2ztPz3EqktNQwQWa7Al8/d42c517c10fcbcb3c0da00bd5fe6b26e/picsart-glass-whale.png?w=3840&q=90&fm=webp)。
- fal：[编辑前](https://images.ctfassets.net/kftzwdyauwt9/50IFJAzURDJeFT6j7jU9Cy/727871e6953a56bebb783f7c884f832f/images-2-6-fal-before.png)、[编辑后](https://images.ctfassets.net/kftzwdyauwt9/mOBUDnc6RlTLi1KU5S19r/2646cf2f1db9cfdf93250f201e8ab5de/images-2-6-fal-after.png)。
- Sable：[产品场景](https://images.ctfassets.net/kftzwdyauwt9/1gnp2Va1JsQtynPds90I1O/3ba2c60fd06e70d9a4dc19da9482ce7d/images-2-6-sable-product-visual.png?w=3840&q=90&fm=webp)。
- Higgsfield：[第 1 步](https://images.ctfassets.net/kftzwdyauwt9/3bU4mZlfoshL05B5nlKuXY/d34032552f29bfef5eeb39533ebe7c61/images-2-6-higgsfield-scene-edit-1.png?w=3840&q=90&fm=webp)、[第 2 步](https://images.ctfassets.net/kftzwdyauwt9/5hDxN1poa1hFkj3ZTSLxqX/42fdc0fc4612cf83a695d63e20abb572/images-2-6-higgsfield-scene-edit-2.png?w=3840&q=90&fm=webp)、[第 3 步](https://images.ctfassets.net/kftzwdyauwt9/3JTfW1LWizYXThKdWaLNrt/a4a9b72ac3ed9909303e594ad0236243/images-2-6-higgsfield-scene-edit-3.png?w=3840&q=90&fm=webp)。
- 旅行视觉：[比较海报](https://images.ctfassets.net/kftzwdyauwt9/6qOP4UgI7SJxKI7mS01b8/dbf9421db5e9ea5a67d8ad8cb219a9df/luxury-travel-updated-poster.jpg?w=3840&q=50&fm=webp)。

## 社区原帖：作者自报 2.6

以下模型信息来自作者，不代表已取得 API 日志或独立复现。均未公开提示词，Sunburst / Flare 未注明。发布日期未从相对时间推断；仅记录本轮核对日期。

1. **community-malfoid**：[夏日角色插画动画](https://www.reddit.com/r/mAIfoid/comments/1xo9cd2/a_little_summer_malfoid_animation/)，u/Junior-Grade-2965。正文明确写使用 ChatGPT Image 2.6，把静态插画变为动画。
2. **community-gifts**：[Images 2.6 brings GIF(T)S :D](https://www.reddit.com/r/ChatGPT/comments/1xo6c69/images_26_brings_gifts_d/)，u/Algoartist。标题明确写 2.6，原帖有媒体；缺少提示词与参数，未独立评价动画效果。

## 媒体报道：等待补齐官方原帖

**reported-dancing-cat**：[The Verge 报道](https://www.theverge.com/ai-artificial-intelligence/1026474/openai-chatgpt-animated-gifs-images-2-6)，2026-11-04。报道描述 OpenAI 的跳舞猫 GIF 演示，并给出提示词：

> can you make a gif of a cat dancing?

模型由报道归为 Images 2.6，具体版本未注明。本轮能读取搜索索引正文，但报道网页直接打开失败；尚未把该演示与下列 OpenAI X 帖精确对应，因此不计入原始来源已核对案例。

## 待核实：不计入已确认案例

| 线索 | 已知情况 | 仍缺什么 |
| --- | --- | --- |
| [OpenAI X 帖](https://x.com/OpenAI/status/2118124958421532806) | 原链接保留；直接读取返回 403 | 帖子内容、具体作品与 prompt |
| [fal X 帖](https://x.com/fal/status/2118127874926407952) | 原链接保留；直接读取返回 403 | 不能将官方发布页的 fal 案例自动视为同一帖子 |
| [Higgsfield X 帖](https://x.com/higgsfield/status/2118134123533623424) | 原链接保留；直接读取返回 403 | 帖子内容及与官方演示的对应关系 |
| [炒饭连续编辑评论](https://www.reddit.com/r/ChatGPT/comments/1xo3oir/comment/19s5jux7atjes/) | u/JoshSimili 给出六步提示词 | 评论未明确实际模型，不能仅因位于 2.6 发布帖而认定 |
| [苏格兰鹿 GIF](https://www.reddit.com/r/ChatGPT/comments/1xo58wn/why_does_chatgpts_new_gif_generator_obsess_over/) | u/alcanthro 描述新 GIF 功能，并附图 | 未明确 2.6、prompt 和完整流程 |
| [尝试新 GIF 功能](https://www.reddit.com/r/ChatGPT/comments/1xo7492/chat_offered_me_to_try_the_new_gif_function/) | u/bonobomaster 发帖附媒体 | 未明确 2.6，未公开 prompt |
| [SoraAi 社区 GIF 帖](https://www.reddit.com/r/SoraAi/comments/1xobgch/chatgpt_now_has_animated_gif_generation/) | u/cool_architect 发帖附媒体 | 作者未明确版本；机器人回复不能作为模型证据 |
| [WittyCommittee GIF 帖](https://www.reddit.com/r/WittyCommittee/comments/1xo9rut/chatgpt_just_got_more_ridiculous/) | u/Dazzling-Skin-308 写 ChatGPT 可做 GIF | 未明确 2.6，未公开 prompt |

## 本轮检索记录与更新方式

- 检索了中英文模型名、提示词、作品、GIF、SVG、编辑案例，以及官方文档、发布伙伴、X 和 Reddit。
- 排除了发布前的传闻页、只给通用模板的营销页、实际使用 2.5 的案例，以及微软 MAI-Image-2.6。页面出现“2.6”不等于结果由 OpenAI GPT Image 2.6 生成。
- 后续按原帖 URL 与本页 ID 去重。新证据可把待核实线索移入对应来源分区，保留作者、核对日期、提示词可用性和模型归因。
- 取得可收录的完整 prompt、必需输入和合适使用条件后，再按[贡献指南](../CONTRIBUTING.md)添加到提示词数据并重新生成页面。不会用改写文本冒充原 prompt，也不会将链接索引的数量混入可复制提示词计数。
