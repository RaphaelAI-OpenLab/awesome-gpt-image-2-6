# Media provenance and availability / 素材来源与获取状态

Checked 2026-11-05 (UTC). This records actual provenance, file formats and availability. It is not a permission grant or legal advice.

核查日期：2026-11-05（UTC）。本页记录真实来源、文件格式与获取结果，不构成授权或法律意见。

## Archival approach / 收录方式

Publicly retrievable example files are stored unchanged with the exact media URL, creator credit, source page, SHA-256 checksum, byte size and actual MIME type. `source-attributed` means an attributed archival copy for this educational collection; an explicit redistribution license was not located. It does not mean MIT/CC-licensed or creator-approved. The homepage educational/takedown notice does not create a license.

可正常获取的公开案例文件原样入库，并记录准确素材链接、作者、来源页面、SHA-256、字节数与实际 MIME 类型。`source-attributed` 表示为本教育用途合集保存、标明来源的副本，未找到明确转载许可证；不代表 MIT/CC 许可或原作者授权。首页的教育用途 / 下架声明不自动赋予许可。

Explicit no-redistribution restrictions and access controls must be respected. An unknown license alone is not recorded as an explicit prohibition. Failed access remains a source link; no authentication, access control or anti-bot restriction was bypassed.

明确禁止转载的限制与访问控制必须遵守；“许可未知”不写成“明确禁止”。获取失败的文件保留来源链接，不绕过登录、访问控制或反爬限制。

This update adds 81 files to the three already archived, for 84 local media files: 69 documentation files, 13 launch-page files and two community previews. Fifteen are labelled reference inputs. Nine direct media requests failed with HTTP 403.

本次新增 81 个文件，连同已有 3 个，共 84 个本地素材：69 个文档素材、13 个发布页素材、2 个社区预览。其中 15 个标为参考输入；9 个直接素材请求返回 HTTP 403。

## Official documentation and launch / 官方文档与发布案例

- [OpenAI image prompting guide](https://developers.openai.com/api/docs/guides/image-prompting): matched assets to the exact case section and the GPT Image 2.6 tabs. Older 2.5 outputs are excluded. Reference/input images are explicitly labelled and stored separately from outputs.
- [Images 2.6 announcement](https://openai.com/index/introducing-images-2-6/): preserves the credited OpenArt, Town, Picsart, fal, Sable and Higgsfield demonstrations. Source-page publication does not establish that OpenAI owns or freely licenses partner works.
- No asset-specific press-reuse license or explicit no-republication notice was located in these sources. [OpenAI brand guidelines](https://openai.com/brand/) govern marks; they do not grant a blanket license to demonstration images. Output-ownership terms do not assign other creators' outputs to readers.
- Downloaded raster files were decoded and contact sheets visually checked. These checks establish file identity, not model reproduction. Static animation posters are labelled `poster`, not GIF files. Original bytes are preserved, including WebP responses from CDN URLs with PNG/JPG names.

官方文档按具体章节与 2.6 标签匹配，排除旧版 2.5 输出。输入 / 参考图单独标注和存放。发布页的合作方作品保留原作者署名，没有把发布于 OpenAI 网站等同于 OpenAI 拥有全部版权或授予开放许可。未找到针对这些素材的转载许可证或明确禁止转载说明。已解码并查看栅格图片联系表；此检查不代表模型复现或动画播放评估。

## Four community examples / 四个社区案例

Original posts:

- [pixexid: bear comparison](https://x.com/pixexid/status/2118153375464505689)
- [Archiefff: boxing tiger](https://x.com/baiji57165/status/2118176730079007145)
- [Dheepan Ratnam: animation variants](https://x.com/Dheepanratnam/status/2118138765487100027)
- [Michael Guo: rosebud animation](https://x.com/Michaelzsguo/status/2118134837357744435)

The original posts and visible previews were inspected. Each creator explicitly attributes the work to Images 2.6, but exact prompts and Sunburst/Flare variants were not disclosed. The claims were not independently reproduced. No creator-specific no-redistribution statement was established for these works, and no independent redistribution license was verified.

已查看原帖和可见预览；模型归属仅为作者自报，未独立复现。原始提示词与 Sunburst/Flare 版本未公开。未查到针对这些作品的作者禁止转载声明，亦未核实独立转载许可证。

### Successfully archived / 已入库

- Bear comparison: the second WebP raster preview (`HWUw0tbbkAANo7E`), not the original PNG/SVG file.
- Rosebud: static WebP poster (`HWUgYUbWMAAdp79`), not the MP4 animation.

### HTTP 403: links retained / HTTP 403：保留链接

Normal public-URL retrieval returned HTTP 403 for nine files. They were not archived and were not retried through bypasses:

- Bear first preview: `HWUw0tfaQAAol4Q`.
- Boxing tiger MP4 and poster: `HWVGfUja0AA4Mww`.
- Hummingbird MP4s: `HWUjhD1WoAA4H3e`, `HWUjjV8WEAA1Msj`, `HWUjlaLW0AAZPL5`, `HWUjnGlWsAA1ptO`; first poster: `HWUjhD1WoAA4H3e`.
- Rosebud MP4: `HWUgYUbWMAAdp79`.

Exact URLs remain in each case's media records. The X animations are MP4, even when the interface labels them GIF. No MP4 was renamed or converted to a GIF. The two pre-existing Reddit cases still lack a verified downloadable asset URL; previously blocked Reddit access was not bypassed.

准确素材地址保留在逐项记录中。X 界面标为 GIF 的动画链接实际是 MP4，没有改后缀冒充 GIF，也未转换格式。两个既有 Reddit 案例尚无核实的可下载素材链接，没有绕过此前的访问限制。

### Platform and creator terms / 平台与作者条款

- [X Terms of Service](https://x.com/en/tos), effective October 9, 2026: creators retain rights. Section 4 requires reproduction/distribution/display to follow X-provided interfaces/instructions subject to permitted uses, and restricts unauthorized scraping. This is not a literal blanket prohibition on every download, nor a redistribution license. Accessibility of a CDN URL is not proof of permission.
- [Pixexid license](https://pixexid.com/license) and [terms](https://pixexid.com/terms): CC BY 4.0 applies to publicly published Pixexid-site images. A matching licensed page for this X comparison was not established, so CC BY 4.0 is not applied to it.

X 的平台条款不是对所有下载的一概禁令，也不是给本仓库的转载许可证；公开 CDN 链接可访问不代表授权。Pixexid 站内许可不能未经对应作品核实就套用于 X 图片。
