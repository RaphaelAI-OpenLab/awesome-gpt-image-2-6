# Opusly / CubistAI / Flixly model-evidence recovery

Reviewed 2026-11-08 UTC. **Ten existing historical candidates** are recovered: Opusly six, CubistAI three and the existing Flixly six-GIF collection as one record. No new cases were searched or substituted. **Fifteen unchanged publisher-served files, 11,645,244 bytes**, are archived: twelve GIFs and three JPEG previews.

These candidates had been held because recovered primary evidence was insufficient, not because a model mismatch had been proved. Their already-known pages now provide work-specific model/example descriptions and source-linked prompts. Model/backend attribution remains the publisher's claim, not an independently observed or reproduced API call.

## Opusly: six existing GIF candidates

Source: [known GPT Image 2.6 maker page](https://www.opusly.ai/gpt-image-2-6).

The page explicitly describes every displayed GIF as a real result of its adjacent prompt made using this tool. Its methods identify GPT Image 2.6 Flare, medium quality, and six test calls. The six exact sample URLs match the previously collected candidates; the current GIF bytes also match their historical SHA-256 hashes and lengths.

| Existing ID | Output |
| --- | --- |
| `opusly-hi-loop` | Chibi greeting character waves below Hi text. |
| `opusly-cat-loop` | Top-hat orange cat dances below TGIF text. |
| `opusly-corgi-loop` | Party-hat corgi hops and wags its tail. |
| `opusly-anime-loop` | Anime portrait blinks while hair and ribbon move. |
| `opusly-knight-loop` | Armored knight walks in place on transparency. |
| `opusly-coffee-loop` | Illustrated steam and rain move beside a coffee cup. |

Each original GIF is 512×512 with eight frames at 150 ms/frame, totaling 1.2 seconds per cycle. All 48 frames were inspected. The site credits public X posts as ideas; these records attribute the actual served files to Opusly, without claiming they are the referenced users' original files. We did not follow those X links. The greeting example's original reference photograph is not provided, and no identity is inferred.

## CubistAI: three named examples

Source: [known Chinese model page](https://cubistai.app/zh/ai-models/gpt-image-2-6).

The exact espresso-cup, botanical-poster and paper-cut-cabin examples each have GPT Image 2.6 labels, corresponding image elements and adjacent prompts. This is stronger than inferring a model from a generic page title alone. Flare versus Sunburst is not established for the individual outputs, so variants remain unspecified.

- `community-cubistai-espresso-cup`: ceramic espresso cup on travertine, 1024×768.
- `community-cubistai-botanical-poster`: botanical exhibition layout, 768×1024.
- `community-cubistai-paper-cut-cabin`: layered paper-cut landscape, 1024×768.

The precise served-image URLs were used without inventing raw asset locations. Although their embedded original asset names end in WebP, the actual responses are JPEG previews. They are saved as JPEGs with unchanged bytes. These three files were obtained during this check for the already-existing candidates; they are not claimed to match a previously retained media hash.

## Flixly: one retained six-test collection

Source: [known six-GIF article](https://www.flixly.ai/blog/gpt-image-2-6-gif-maker).

The article explicitly describes the displayed files as six tests made on Flixly, with work-specific model captions and prompts. Preserve the existing ID `flixly-six-gif-tests` as one collection rather than inflating it into six newly counted cases.

| Original file | Publisher model label | Decoded size and timing |
| --- | --- | --- |
| `fox.gif` | Sunburst | 512×512, 16 frames, 100 ms/frame, 1.6 s |
| `coffee.gif` | Sunburst | 768×432, 9 frames, 200 ms/frame, 1.8 s |
| `neon.gif` | Flare | 768×432, 9 frames, 200 ms/frame, 1.8 s |
| `sticker.gif` | Sunburst | 512×512, 9 frames, 200 ms/frame, 1.8 s |
| `snow.gif` | Flare | 432×768, 9 frames, 200 ms/frame, 1.8 s |
| `mira.gif` | Sunburst Edit | 432×768, 9 frames, 200 ms/frame, 1.8 s |

All 61 frames were inspected. Files were obtained now from the existing candidate's primary page and retained unchanged, including transparency and visible motion imperfections. The article's first-result, unchanged-output, quality and runtime assertions are publisher claims. Its text-to-GIF/editing capabilities were not independently tested. It calls Mira an edit of an earlier portrait, but this review does not establish the exact input file and does not guess one from other comparisons. The generated character name is a source label, not identification of a real person.

## Still held: two APIMODELS paper-boat candidates

The existing [Flare](https://apimodels.app/zh/models/gpt-image-2.6-flare) and [Sunburst](https://apimodels.app/zh/models/gpt-image-2.6-sunburst) page URLs both returned HTTP 200, but their current galleries do not contain the historical paper-boat examples or their old media links. Current pages show different works. Those works are not substitutes and were not collected as new cases. `apimodels-flare-paper-boat` and `community-apimodels-sunburst-paper-boat` remain outside the published increment pending work-specific evidence.

## Verification and rights

All fifteen file requests succeeded. All three stills and all 109 GIF frames were decoded and visually reviewed. Full prompts remain source-linked rather than copied. No raw source pages, QA contacts or rasterized/modified derivatives are published. Build, schema/asset validation, generated-file consistency, regression tests, duplicate screening and additive replay checks are required before release. The 349-case main baseline is preserved; replay rejects differing existing records before writing and is idempotent.

No explicit redistribution licence was verified. Public access and source attribution are not permission, and the repository's MIT licence does not cover third-party media. Provider claims are not independent model authentication, rights clearance or performance benchmarks.
