# STRUGGLE 既有案例来源核对

核对日期：2026-11-08。本文保留当日报告中的六个 STRUGGLE 案例，准确来源和现行素材元数据见 `content/source-cases.json`。

## 作品依据

- STRUGGLE_xlf: the author explicitly describes running five test groups on their own account and supplies the individual prompts/results. Six existing cases cover two text-to-GIF examples, one photo-to-GIF workflow, one two-stage poster edit, one SVG logo and one perfume product image. These are creator-reported Images 2.6 attributions, not independent API logs. The Flare/Sunburst variant is not established.

六个案例的公开原文提示词使用 `source-only` 状态；模型归属为作者自述，不代表独立 API 执行验证。

## 当日素材核对记录

- The 4284×5712 desk reference JPEG contains location metadata. It remains link-only; no coordinates or original reference bytes are republished or included in the deliverable backup. The eight-frame 267×716 output GIF is archived.
- The second poster image is represented by an article failed-transfer element that preserves its original URL. That exact URL returned HTTP 403. It was not retried, no alternate route was used, and it remains link-only. The first poster image is archived; the two stages remain one case.
- Three actual GIF files contain 9, 9 and 8 frames. All 26 frames were decoded and inspected, together with the static images. No timing or quality benchmark is claimed.
- The original SVG is a rectangle and three paths, with title/description. XML security checks found no script, event attributes, foreign objects, raster payloads or external dependencies; its offline render was inspected. It was downloaded as an SVG, not reconstructed from article code.

## 来源与使用状态

素材保留准确来源、作者及逐项使用限制。公开访问与署名不等于取得转载许可，仓库 MIT 协议不覆盖第三方素材。
