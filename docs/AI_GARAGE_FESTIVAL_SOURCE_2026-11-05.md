# Shiba chef festival background edit: source and media notes

Case: `ai-garage-festival-background`

## Original source / 原始来源

- Author / 作者: Seiya Yagashiro / ai-garage.
- [Original report / 原始报告](https://ai-garage.jp/news/gpt-image-2-6-flare-sunburst-api-test/), published November 5, 2026.
- [Original comparison image / 原始对比图](https://ai-garage.jp/images/article-figures/gpt-image-2-6-flare-sunburst-api-test-3.webp).

The report describes the author's own API tests with `gpt-image-2.6-flare` and `gpt-image-2.6-sunburst`. Its background-edit section publishes the short edit instruction and the comparison image. The image labels the original input at left, the Flare edit in the middle and the Sunburst edit at right. This is one source-linked comparison case, not three separate generated outputs.

原文描述作者自行进行的 GPT Image 2.6 Flare 与 Sunburst API 测试。背景编辑章节公开简短编辑指令及对比图。图中左侧为原始输入，中间为 Flare 编辑结果，右侧为 Sunburst 编辑结果。本条收录一个来源对比案例，不把三联图计作三张生成结果。

This is the creator's model attribution, not an independently reproduced generation. The published edit instruction remains linked at the source; no complete prompt or generation parameters are invented here.

这是作者自报的模型归因，非整理者独立复现。公开编辑指令链接原文，不补写完整提示词或生成参数。

## Access and local checks / 获取与本地检查

- Original-page check: November 5, 2026. The public page and model attribution were readable without login.
- Recorded original-image request: HTTP 200, `image/webp`, 210,864 bytes.
- Archived file: [`source-01.webp`](../assets/examples/ai-garage-festival-background/source-01.webp), unchanged original bytes, 1876 × 469 pixels, one static frame.
- SHA-256: `7063e40eb7b3fd683d9ff0b8e2f2b24c4e913f2775e96d12cb017d990a6bbc28`.
- Local review: November 6, 2026. File size, SHA-256, WebP decoding, dimensions and visible panel labels checked against the retained original source. No EXIF or XMP metadata was found. No new source request or model generation was made for this review; current remote availability was not rechecked.

原页面与素材的获取记录来自 2026 年 11 月 5 日。2026 年 11 月 6 日仅检查已保留的原始材料与本地文件，未重新请求来源或调用生图模型，不将此次本地检查表述为最新在线可用性验证。

## Reuse status / 使用状态

`source-attributed`: an unchanged public-source archive with the original author's credit. No explicit redistribution license was verified and no explicit redistribution prohibition was found in the reviewed evidence. Public availability and attribution do not grant permission or establish an open license. The repository MIT license does not cover this third-party media.

`source-attributed` 表示原样收录公开来源文件并注明作者，未核实明确转载许可证，已审阅证据中未发现明确转载禁令。公开可见与署名不构成许可或开放授权，仓库 MIT 许可证不覆盖此第三方媒体。
