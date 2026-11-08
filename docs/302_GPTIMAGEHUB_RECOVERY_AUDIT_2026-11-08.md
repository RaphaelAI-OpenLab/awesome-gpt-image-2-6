# 302.AI / GPT Image Hub retained-case audit

Reviewed on 2026-11-08 UTC. This batch contains **15 existing local cases, 29 original files (35,816,503 bytes)**. It resolves the previously pending 302.AI eight and GPT Image Hub seven cases by checking their already-known primary pages. No new case search was performed.

## Evidence and verification

- The five known source/model pages returned HTTP 200. The 29 already-retained media URLs also returned HTTP 200, with exactly matching SHA-256 hashes and byte counts. Unchanged bytes are archived in this repository; source URLs remain recorded beside each file.
- All 27 still images and every frame of the two GIFs (9 frames each, 18 total) were decoded and visually inspected. Both GIFs have 200 ms frame durations, 1.8 seconds per cycle. QA contact sheets and raw page captures are not published.
- Formats are 16 PNG, 5 JPEG, 6 WebP and 2 GIF files. The file roles are 26 outputs and 3 reference composites. A comparison pair, an edit workflow or a GIF is one case, not one case per image/frame.
- Model attribution means the publisher explicitly associates the work with the named model. We did not independently observe the generation API calls or reproduce the examples. Provider settings, costs, speeds and quality rankings are not verified benchmark results.

## 302.AI: eight cases

Primary article: [302.AI Benchmark Lab review](https://302.ai/blog/302-ai-benchmark-lab-review-on-gpt-image-2-6-flare-and-sunburst/). The article describes the publisher's own API debugging tests, consistent prompts/reference images, first-returned results, xhigh quality and high complexity. These remain publisher claims.

| Case ID | Evidence / counting boundary |
| --- | --- |
| `302-lumiere-jewelry-portrait` | Two outputs have directly adjacent Flare and Sunburst labels. The neighboring Gemini output is excluded. |
| `302-y2k-orange-fashion` | One fashion prompt, two explicitly labelled model outputs. No claim of proven identity consistency. |
| `302-vhs-drift-race` | One prompt, two explicitly labelled static images. Timestamps and recording noise are fictional design elements, not real race footage. |
| `302-ink-wolves-snow` | One illustration prompt, two explicitly labelled outputs. No artist endorsement is implied. |
| `302-block-world-cover` | Two labelled outputs plus one reference composite. Text naming other models inside the artwork is not generation evidence. |
| `302-group-photo-environment-edit` | Two labelled outputs plus one two-photo reference composite. Synthetic edit, not an authenticated event photograph; no people are identified. |
| `302-halftone-meow-loop` | Two GIFs in one prompt section. The page does not explicitly map each file to Flare or Sunburst, so the specific variant remains unspecified. |
| `302-flying-car-collage` | Two outputs plus one five-view reference composite. The individual output variants are unspecified. Vehicle performance, product-release text and brand imagery are not factual product claims or endorsement. |

For the six labelled tasks, file attribution follows the text directly preceding the file, not visual style or order alone. For the two unlabeled pairs, the family attribution is supported by the article's task context but no file-level variant is inferred. Other uncollected illustrations on the article are not added. Exact original prompts are linked at the article sections, not republished here.

## GPT Image Hub: seven cases

Known pages checked:
- [Prompt guide](https://www.gptimagehub.com/guides/how-to-prompt-gpt-image-2-6)
- [General guide](https://www.gptimagehub.com/guides/gpt-image-2-6)
- [Flare Saver model page](https://www.gptimagehub.com/models/gpt-image-2-6-flare-saver)
- [Sunburst Saver model page](https://www.gptimagehub.com/models/gpt-image-2-6-sunburst-saver)

Individual captions/alt text and exact image paths associate the examples with the provider's named routes. “Saver” is the provider's service label, not independently verified evidence of a separate official OpenAI model. The model pages describe their examples as generated or edited on GPT Image Hub on 5 November 2026.

| Case ID | Evidence / counting boundary |
| --- | --- |
| `gptimagehub-structured-coffee-poster` | Vague/structured comparison, one case. Both captions name Flare and 1024×1536/high generation settings; retained served previews are actually 667×1000 JPEGs. |
| `gptimagehub-amalfi-poster` | Flare page, travel-poster output and source-linked prompt. |
| `gptimagehub-coffee-bean-infographic` | Sunburst page, infographic output and source-linked prompt. |
| `gptimagehub-sage-speaker` | Flare page, product-image output and source-linked prompt. |
| `gptimagehub-ember-isles-map` | Sunburst page, fictional-map output and source-linked prompt. |
| `gptimagehub-ramen-rain-snow` | One Flare workflow. Both are provider-attributed outputs; the rain image is reused as the snow edit's input. Only the edit instruction is public in the reviewed page, not the initial image's exact prompt. |
| `gptimagehub-moonleaf-tea-edit` | One Sunburst workflow, jasmine packaging and rose-label edit. The page supplies the initial prompt and short editing instruction; the first output is reused as the input. |

The six model-page examples link directly to the corresponding model page instead of relying on a general product announcement. Served preview formats and dimensions are taken from file decoding, not filename suffixes or advertised generation settings. Already-collected examples elsewhere in the guides are excluded.

## Deduplication and release checks

The 15 IDs are absent from the 269-case main baseline after PR #32. IDs and original media URLs are compared with the baseline and other locally available accepted increments. SHA-256 is compared against all recovered records. A first-frame perceptual screen checks other decodable retained files; it is a candidate screen, not proof that two workflows are distinct. Build, validation, generated-file consistency, the test suite and additive replay checks are required before release. The replay rejects conflicting existing records before writing and preserves unrelated newer records.

## Rights and limits

No explicit redistribution licence was verified for these third-party files. Public availability and source attribution do not establish permission. The repository's MIT licence does not cover these media. All original marks, reference-image composites and synthetic design text are retained without alteration; no QA derivative is included. Model attribution and original-prompt access are distinct from copyright permission.
