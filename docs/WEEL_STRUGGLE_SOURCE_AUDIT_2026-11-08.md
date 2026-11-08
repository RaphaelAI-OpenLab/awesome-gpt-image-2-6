# WEEL and STRUGGLE existing-case source audit

Reviewed 2026-11-08. Seven existing local candidates are added; all 349 prior records remain unchanged. Two existing original article URLs returned HTTP 200. No new-case search or model-generation run was performed.

## Work-specific evidence

- WEEL: its own hands-on Images 2.6 section identifies a saved mug input, three Japanese prompts and three corresponding cafe, picnic and ecommerce outputs. The four original PNGs match the exact full-size URLs in the current article image srcsets. This remains one workflow, not four cases. The author notes unrequested coffee in two scenes; no exact-pixel identity guarantee is made.
- STRUGGLE_xlf: the author explicitly describes running five test groups on their own account and supplies the individual prompts/results. Six existing cases cover two text-to-GIF examples, one photo-to-GIF workflow, one two-stage poster edit, one SVG logo and one perfume product image. These are creator-reported Images 2.6 attributions, not independent API logs. The Flare/Sunburst variant is not established.

All seven prompt statuses are source-only because the actual prompts are public at the linked original source. Long prompts and full-page captures are not copied into the repository. General model/API/price claims elsewhere in either article are not treated as evidence for these outputs.

## Files and exceptions

Twelve recorded source assets were mapped to current article elements. Eleven current media requests returned HTTP 200 with byte-identical originals; one returned HTTP 403. Ten safe, accessible originals are archived unchanged.

- The 4284×5712 desk reference JPEG contains location metadata. It remains link-only; no coordinates or original reference bytes are republished or included in the deliverable backup. The eight-frame 267×716 output GIF is archived.
- The second poster image is represented by an article failed-transfer element that preserves its original URL. That exact URL returned HTTP 403. It was not retried, no alternate route was used, and it remains link-only. The first poster image is archived; the two stages remain one case.
- Three actual GIF files contain 9, 9 and 8 frames. All 26 frames were decoded and inspected, together with the static images. No timing or quality benchmark is claimed.
- The original SVG is a rectangle and three paths, with title/description. XML security checks found no script, event attributes, foreign objects, raster payloads or external dependencies; its offline render was inspected. It was downloaded as an SVG, not reconstructed from article code.

## Attribution, rights and deduplication

Each file retains its precise source, creator and rights limitations. No explicit redistribution licence has been verified. Source attribution and public visibility are not permission; repository MIT terms do not cover third-party media. Character, logo and other third-party rights may apply.

The seven IDs, twelve exact media URLs and ten archived hashes were checked against the current published set and the other recovered candidates. First-frame perceptual screening found no close matches at a 64-bit difference-hash distance of five or less. This is a screening aid, not proof of originality.

Sharkly remains pending after its original article returned HTTP 403. No retry or alternative access route was used. It is not included in the published count or this incremental archive.

The unchanged generator, validator and 44-test suite are run. The incremental replay preserves existing cases, is idempotent and refuses conflicting records/files before mutation. No separate second-reviewer audit has been completed.

## 中文摘要

补核已有 WEEL 一条、STRUGGLE 六条，逐项对应原文实测、提示词与素材，不搜索新案例。保留来源自述和版本未知的边界。10份原件可公开存档；桌面输入照片因位置元数据仅链接，第二张海报因403仅链接且不重试。Sharkly仍待核验。所有既有349条保持不变。
