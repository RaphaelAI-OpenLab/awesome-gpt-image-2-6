# Sogni, OmniaKey and SandBase: recovered source review

Eight source-attributed cases reviewed offline on 2026-11-08 from original source material retained on 2026-11-05, exact asset manifests and original media. This pass made no new source searches, media requests, model runs or timed playback. Retained access does not establish current availability. Provider model labels and measurements are claims, not independently verified backend executions or benchmarks.

## Sogni: three examples

[Original article](https://blog.sogni.ai/blogs/gpt-image-2-6/)

The retained Sogni Labs article is dated November 4, 2026. The bakery poster is individually labelled GPT Image 2.6 Flare, Medium quality. The publisher reports serial API calls on November 4 PT, one take per prompt, 1024-square JPEG, Medium quality and High complexity. No exact bakery prompt is present in the reviewed page. The 2.5 counterpart and merely discussed solar-system/watch results are not added.

The two monkey-lantern GIFs are individually labelled Sunburst and Flare. Both original files contain nine 896 × 896 frames at 200 ms. The source gives the Sunburst motion prompt but says only that Flare used a similar prompt, not necessarily the same one. Sunburst is therefore `source-only`; Flare and the bakery poster are `not-public` in the reviewed source, not a claim about availability elsewhere. The two animations are visibly different runs, with different clothing and framing; they are not duplicate copies of the official example. Every frame was decoded and visually inspected. Timing, cost and quality comparisons remain publisher claims from a small sample.

## OmniaKey: three workflows

[Original article](https://omniakey.com/blog/gpt-image-2-6-review)

The retained original English article credits Kiki, COO / OmniaKey, and is dated November 5, 2026. It says the author ran these examples once per setting through OmniaKey's API with no retries or selection. This is attributed, not independently reproduced.

- The paper-cut fox is explicitly linked to a request naming `gpt-image-2.6-sunburst`. Its exact original prompt is available at source. The unchanged GIF is 669,897 bytes, 433 × 395, with nine frames at 180 ms. The request asked for 200 ms; both source and file support this discrepancy. The contact sheet is not another case.
- The Port Calder comparison remains one case with three outputs: Sunburst/low complexity, Sunburst/high complexity and Flare/high complexity. All three WebPs are 1024 × 1536, matching their adjacent labels. The shared original prompt is public. One run per setting cannot establish that complexity caused the differences. Source timing and text-accuracy judgments are not independent benchmarks.
- The bottle edit remains one workflow. The article identifies the sage-green input as Flare and the terracotta edit as Sunburst. The input is a reference, not an additional output case. The article paraphrases the creation/edit instructions rather than supplying verbatim full prompts, so prompt status is `not-public` in that source. Both WebPs are 1536 × 1024. The background looks similar, but the publisher's SSIM figures are not independently reproduced and do not imply pixel identity.

## SandBase: two comparison boards

[Original article](https://blog.sandbase.ai/gpt-image-2-6-flare-sunburst-api-2026/)

The original page's retained browser extraction includes its full visible article text, image URLs and alt descriptions, credited to Evelyn Park and dated November 5, 2026. This is primary page content, not only an older audit summary. It identifies the tea poster pair as Flare left / Sunburst right, and the edit board as Flare-generated base left / Flare edit middle / Sunburst edit right. The exact archived PNG URLs and hashes come from the dated collection manifest. The browser extraction retains the corresponding WebP previews and the `Original PNG` link text, but not the PNG anchor targets; this limitation is explicit rather than presented as an exact-URL match in the raw extraction.

The original PNG boards are 2064 × 1280 and 3104 × 1280: respectively two or three 1024 × 1280 panels with 16-pixel gutters. Their visible subjects, panel order, edits and file sizes match the original page descriptions. They remain two workflows, not five separate generated cases. The panels were not recropped or resized for the archive. The shared Flare input is not counted as a new generation in the editing case.

The article describes its poster brief and editing request, but the exact full run prompts are not provided. A nearby curl example has different settings and a shorter instruction, so it is not substituted for the original test prompt. Both cases remain `not-public` in the reviewed source. Provider timing and pixel-difference measurements remain attributed and were not rerun.

## File checks, rights and held work

Eleven unchanged original files total 15,928,941 bytes: three GIFs, one JPEG, five WebPs and two PNG comparison boards. SHA-256 and byte count match both the recovered records and dated original-file manifests. Formats, dimensions and full decoding were checked. All eight static files and all 27 GIF frames were visually inspected. No GPS EXIF was detected. Original metadata and bytes remain unchanged; no cryptographic authenticity verification is claimed.

Accepted IDs, original asset URLs and hashes were checked against the PR #26 baseline and the prepared #22 and Recraft/JZ increments. Additional exact-hash and first-frame similarity screening covers the recovered collection and is saved with the replay package. This is not comprehensive transformed-image deduplication. Source comparison panels are not independently counted as multiple cases.

No explicit redistribution license was verified. Attribution, public access and commercial-use terms for customers do not grant a public sample-file license. These are source-attributed files, excluded from the repository MIT license. No current access or legal review was performed. Historical access limitations were not retried or treated as copyright findings.

Three remaining AI Videos candidates are held outside this published increment. Their original article capture was not recovered; an older review and original asset manifest do not replace missing primary evidence. Their files are preserved separately with provisional model attribution and unverified prompt status.

中文：本批八条以原始页面材料和准确资产清单作来源归因，非独立复现。Sogni 三条分别保留明确变体及不同提示词公开状态；OmniaKey 三组按工作流组织，不把对比版本或输入重复计数。SandBase 两张原始对比拼图通过保留正文、面板描述和准确文件清单对应，但浏览器提取未保留 PNG 链接目标，已明确说明此证据边界。十一份原文件核对哈希与大小，八张静图和二十七帧全部目视复核。未确认转载许可证，署名不等于授权，MIT 不覆盖第三方媒体。AI Videos 三条缺原文快照，单独待核验。
