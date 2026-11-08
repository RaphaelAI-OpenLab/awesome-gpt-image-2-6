# AI Videos / YepShot retained-case audit

Reviewed 2026-11-08 UTC. This batch resolves **51 existing local cases: AI Videos 3 and YepShot 48**, retaining **52 publisher-served files, 8,343,759 bytes**, unchanged. Only known original pages and the media associated with these existing cases were checked. No new case search or image generation was performed.

## YepShot: resolving the 2.5 / 2.6 evidence conflict

The [known primary comparison page](https://yepshot.com/nano-banana-2-1-vs-gpt-image-2-6) returned HTTP 200. It explicitly says it was updated on 6 November 2026 and describes 48 GPT Image 2.6 Flare runs on that date via fal.ai, medium quality, automatic aspect ratio and 1K settings. It says each model ran once per prompt; Nano Banana ran in October, on different days. These are publisher-reported examples, not independently reproduced backend runs or a controlled benchmark.

This current primary evidence resolves the gap in the older retained article, which described a GPT Image 2.5 comparison and had not yet run 2.6. We do not relabel that older test. The current page provides separate, work-specific GPT Image 2.6 labels and exact full-size file links for all 48 retained results.

For every case, the current image element says “GPT Image 2.6 result” and its containing link points to the exact retained `/explore/...-after-gpt26.webp` URL. All 48 original URLs returned files with identical historical SHA-256 hashes and byte counts. The page also serves smaller `/compare/gpt-image-2-6/...` thumbnails. Those are different compressed files and are not substituted for the original retained assets.

Counting and limitations:
- One case per distinct source-photo/edit task, not one case per comparison column. Only the 48 GPT Image 2.6 outputs are archived in this batch. Reference photographs and Nano Banana outputs are not copied or counted as GPT outputs.
- Exact prompts live on separate Explore pages. This recovery review did not inspect those pages or reconstruct prompts from pictures or titles, so prompt status remains unverified for the 48 cases.
- The publisher says eight brushed edits used automatically drawn guide masks, not the newer markup layer. Per-case mask assignments are not independently established.
- The publisher reports blurring real book titles in `yepshot-lifestyle-bright-living-room`, a headset logo in `yepshot-lifestyle-neon-gaming-desk`, and a toy-maker logo in `yepshot-creative-collectible-figure`. We preserve those published, edited files unchanged and do not describe them as untouched raw generations.
- Labels such as “ID photo” describe an image-editing example, not a verified identity document or proof of acceptance by an authority. People in the examples are not identified.
- The “erase barcode/watermark” example is a publisher's existing editing result. This batch does not remove marks, alter originals or establish permission to remove third-party rights information.

All 48 are single-frame WebP images. Output size and appearance were checked from actual files, not inferred from advertised model capabilities. The individual catalog entries carry their own exact source/media links and descriptions.

## AI Videos: three cases

The [known original article](https://aivideos.eu/blog/gpt-image-2-6) returned HTTP 200 and provides first-person test descriptions by Richard Byrne. Model and timing/cost claims remain the author's claims.

1. **`aivideos-flare-headline-edit`**: The article explicitly describes feeding its Sunburst film-week poster to Flare's edit endpoint and changing the headline to “STUDIO NIGHTS”. The exact edit instruction is public. One 1088×608 WebP output is archived. The original Sunburst input remains a source-only reference link, not another output. The broad composition-retention description is not proof of pixel-identical preservation.
2. **`aivideos-neon-reel-gif-comparison`**: One comparison case, two original GIFs: nine frames at 832×832 and 120 ms/frame (1.08 seconds), and sixteen frames at 512×512 and 80 ms/frame (1.28 seconds). The variant is unspecified, and the exact full prompt is not supplied in the reviewed article. The current page now displays animated WebP versions, not direct GIF links. Those current files were inspected alongside every retained GIF frame: dimensions, frame counts, timing, visual sequences and transparency shapes match. Their color pixels and encodings are not identical. The known historical GIF URLs still return the exact retained GIF bytes. This source-format boundary is disclosed rather than claiming a current direct GIF link. Transparent edge patches are retained, not repaired or hidden.
3. **`aivideos-clapperboard-svg`**: The exact SVG URL is still on the article, labelled as a GPT Image 2.6 clapperboard/play-button logo. Variant unspecified; exact full prompt not supplied. The 1,463-byte file has a 1024×1024 viewBox and red, near-black and white elements, although the author says two colors were requested. XML inspection found no scripts, event handlers, entities, external resources, URL references or active embedded elements. It was locally rendered for visual inspection; the unchanged SVG, not the QA rasterization, is published.

All four retained AI Videos file URLs returned HTTP 200 and identical historical SHA-256 hashes and byte counts. The current WebP animation derivatives were used only for verification and are not counted or republished as additional cases.

## Verification and integration

- Reviewed 49 still images, every one of the 25 GIF frames and the SVG rendering. The two current WebP animations were also compared frame by frame. No fresh timed browser-playback or independent model-generation claim is made.
- Checked IDs and original media URLs against the 295-case main baseline after PR #34 and locally available accepted increments. Checked exact media hashes against the recovered inventory. Perceptual first-frame screening is supplementary, not exhaustive transformed-repost detection.
- Build, validation, generated-output consistency and all regression tests are required before release. Additive ID-based replay is tested for equality, idempotence and rejection of differing existing records before any writes. Existing baseline records are preserved.
- Raw web pages, long original prompts, source-only reference files and QA contact sheets are not included in the public increment.

## Rights

No explicit redistribution licence was verified. Public availability and attribution do not establish permission, and the repository MIT licence does not cover third-party media. Files retain the publisher's original bytes, including the three disclosed YepShot publisher edits and the GIF transparency defects. Source attribution is not independent authentication of the model, depicted events, commercial claims or the people shown.
