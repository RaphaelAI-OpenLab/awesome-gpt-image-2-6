# Prompt card layout reference / 卡片结构占位

This is a layout reference only. Add real records to `content/prompts.json`; do not copy this file into the public collection as an example.

此文件只说明位置，不含真实提示词，也不会被生成器计入案例。

## {{TITLE}}

{{SOURCE_ONLY_OR_TESTED_STATUS}}

{{PREVIEW_IMAGE_OR_ORIGINAL_SOURCE_LINK}}

{{ORIGINAL_SOURCE_URL}} · {{AUTHOR}} · {{SOURCE_DATE}}

### Original prompt / 原始提示词

```text
{{PASTE_THE_ACTUAL_ORIGINAL_PROMPT_HERE}}
```

### Recorded settings / 已记录参数

| Setting | Value |
| --- | --- |
| Model variant | {{SUNBURST_FLARE_OR_UNSPECIFIED}} |
| Quality | {{KNOWN_QUALITY_OR_OMIT}} |
| Complexity | {{KNOWN_COMPLEXITY_OR_OMIT}} |
| Output format | {{KNOWN_FORMAT_OR_OMIT}} |
| Reference images | {{ACTUAL_INPUT_FILES_OR_NONE}} |

{{WORKFLOW_AND_TEST_NOTES}}

Optional website locations / 可选网站入口：

- Case detail page: `links.case_detail_url`
- Verified generation deep link: `links.generate_url`
- Deep-link verification date: `links.generate_url_verified_at`

These are different destinations. The generator displays a generation CTA only after the configuration and record meet the conditions described in `docs/LINK_MAP.zh-CN.md`.
