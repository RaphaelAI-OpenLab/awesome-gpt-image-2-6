# FrameMux and APIXO local backlog audit

Reviewed on 2026-11-08. Adds 11 previously collected workflows (FrameMux 7, APIXO 4) while preserving all 269 published baseline records. No new-case search, media download or generation was performed. Four known primary HTML pages and one existing linked prompt file returned HTTP 200. Relative FrameMux media links resolve to the recorded exact URLs; all APIXO original media links occur in the revisited pages.

## Provenance and boundaries

- FrameMux gallery cards individually carry GPT Image 2.6 labels; the page identifies its default model as Flare. These are platform claims, not independently verified execution. The page publishes the corresponding prompts, which are linked rather than copied.
- The six FrameMux animations are served animated WebP files, six frames at 160 ms each. The platform describes browser assembly from sprite sheets; these are not claimed as native model GIF files. The cat sheet and cat animation share a workflow, without claiming that the exact animation was cut from the displayed sheet. Three companion originals remain input references; filenames naming other models do not establish their provenance.
- APIXO identifies the fox tutorial output as Flare through its MCP, and separately labels the other launch-page fox as Flare. Two different original nine-frame GIFs remain one workflow; the tutorial prompt is not applied to the launch output. All 18 frames were inspected.
- The coffee SVG is 1024-square with 7 paths, 2 ellipses and 1 rectangle. XML checks found no script, events, embedded image, external reference or URL-bearing style. The inert SVG was rendered using the installed local renderer and reviewed beside the publisher PNG. Shape/proportion differences are visible, so the preview and SVG are not claimed pixel-identical. They remain one publisher-associated example.
- The coral-vase composite contains the original OpenAI reference, Flare edit and Sunburst edit from left to right. It is one comparison workflow; the source image is not an extra output. The composite is 1816 × 450, distinct from source-reported individual-output dimensions. No pixel-preservation, speed or superiority claim is independently validated.
- The Daily Pour poster is a fictional event image. Its actual retained format is JPEG despite the .webp URL. Its exact original prompt remains not-public in the reviewed source; none is reconstructed.

## Media and duplicate checks

17 unchanged original files total 2,935,476 bytes: 11 WebPs (six animated), 2 GIFs, 1 SVG, 2 PNGs and 1 JPEG. All 63 frames/stills, including the local SVG render, were visually inspected. The comparison was also inspected at full width. Sizes and SHA-256 match the retained records. No EXIF GPS fields were found in the 16 raster images. No QA render or contact sheet is published.

Exact media URLs and SHA-256 values were checked against the other 629 recovered cases without matches. A 64-bit first-frame dHash screen against 534 decodable earlier files found no pairs within five bits. This screen cannot rule out every crop or semantic repost; unsupported earlier files were excluded from the perceptual check.

## Pending source

The three already-collected SeedRouter cases are excluded. The known original model page returned HTTP 403 Forbidden on 2026-11-08. No retry or alternate route was used. Collector observations alone are not promoted to current primary evidence; draft records and local originals remain pending.

## Rights and validation

All originals remain source-attributed, with author/source links and per-file limits. No independently verified redistribution licence is claimed. Public access and credit do not grant permission; repository MIT does not cover third-party files. Brand marks are artwork, not evidence of affiliation or trademark permission. Full page captures, long prompts and QA derivatives are excluded. No separate second-reviewer audit was completed.

The unchanged generator, validator and 44-test suite are run before submission. ID-based replay preserves existing records, regenerates all 16 README routes and refuses conflicting records/files before mutation.

## Per-file inventory

| Workflow | File | Format / frames | Bytes |
| --- | --- | --- | --- |
| `framemux-sunny-pop-poster` | `assets/examples/framemux-sunny-pop-poster/framemux-gpt-image-2-6-poster.webp` | WEBP / 1 | 83032 |
| `framemux-cat-barista` | `assets/examples/framemux-cat-barista/framemux-gpt-image-2-6-sprite.webp` | WEBP / 1 | 110508 |
| `framemux-cat-barista` | `assets/examples/framemux-cat-barista/framemux-ai-gif-cat-barista.webp` | WEBP / 6 | 85536 |
| `framemux-dinosaur-wave` | `assets/examples/framemux-dinosaur-wave/framemux-ai-gif-dino-wave.webp` | WEBP / 6 | 90068 |
| `framemux-pixel-knight` | `assets/examples/framemux-pixel-knight/framemux-ai-gif-pixel-knight.webp` | WEBP / 6 | 46634 |
| `framemux-window-cat` | `assets/examples/framemux-window-cat/framemux-image-to-gif-window-cat.webp` | WEBP / 6 | 83048 |
| `framemux-window-cat` | `assets/references/framemux-window-cat/framemux-kling-2-6-cat.webp` | WEBP / 1 | 49138 |
| `framemux-moon-bounce` | `assets/examples/framemux-moon-bounce/framemux-image-to-gif-astronaut.webp` | WEBP / 6 | 111342 |
| `framemux-moon-bounce` | `assets/references/framemux-moon-bounce/framemux-grok-video-astronaut.webp` | WEBP / 1 | 65038 |
| `framemux-ramen-steam` | `assets/examples/framemux-ramen-steam/framemux-image-to-gif-ramen.webp` | WEBP / 6 | 152352 |
| `framemux-ramen-steam` | `assets/references/framemux-ramen-steam/framemux-nano-banana-pro-food.webp` | WEBP / 1 | 151360 |
| `apixo-fox-wave-workflow` | `assets/examples/apixo-fox-wave-workflow/apixo-fox-tutorial.gif` | GIF / 9 | 338803 |
| `apixo-fox-wave-workflow` | `assets/examples/apixo-fox-wave-workflow/apixo-fox-launch.gif` | GIF / 9 | 336866 |
| `apixo-coffee-cup-svg` | `assets/examples/apixo-coffee-cup-svg/apixo-coffee-svg.svg` | SVG / 1 | 2183 |
| `apixo-coffee-cup-svg` | `assets/examples/apixo-coffee-cup-svg/apixo-coffee-svg-preview.png` | PNG / 1 | 45841 |
| `apixo-coral-vase-comparison` | `assets/examples/apixo-coral-vase-comparison/apixo-kitchen-comparison.png` | PNG / 1 | 1074994 |
| `apixo-daily-pour-poster` | `assets/examples/apixo-daily-pour-poster/apixo-coffee-poster.jpg` | JPEG / 1 | 108733 |

## 中文摘要

本批复核已有 FrameMux 7 条与 APIXO 4 条，共 11 个工作流。17 份原件、63 帧及静图均检查，全部保留真实格式、参考输入与权利限制。SVG 与发布方 PNG 预览的形状比例不同，不宣称完全一致。SeedRouter 3 条因原页 403 继续待核验，不绕过访问限制。现有 269 条内容不变，未搜索新案例。
