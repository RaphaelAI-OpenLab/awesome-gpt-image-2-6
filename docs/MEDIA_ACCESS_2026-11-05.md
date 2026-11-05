# Source-page and media recheck / 原帖与素材逐项复查

Checked 2026-11-05, 08:50–08:54 UTC. Status is specific to the route and time checked, not a claim of global availability.

核查时间：2026-11-05 08:50–08:54 UTC。状态仅对应当次获取方式与时间，不代表全球可访问性。

## Outcome / 结果

All nine X media files that previously returned HTTP 403 to direct HTTP requests were saved successfully through the normal public browser. Added **6 MP4 videos and 3 WebP images/posters**. The repository now contains **93 local media files**, across **41 of 43 cases**. Existing files were not changed.

此前直接 HTTP 请求返回 403 的九个 X 素材，本次均通过正常公开浏览器成功保存，新增 **6 个 MP4 和 3 张 WebP 图片 / 海报**。仓库现有 **93 个本地素材文件**，覆盖 **43 个案例中的 41 个**。既有素材未改动。

The earlier media-request failures did not mean the original posts were inaccessible. Both exact Reddit post URLs, however, currently show an explicit network-security block in this browser. No Reddit media URL was exposed, so direct-media availability remains unknown, not a verified 403 or deletion.

此前失败的是直接媒体请求，不等于原帖打不开。两个准确的 Reddit 原帖地址则确实在当前浏览器显示网络安全拦截。页面未提供素材地址，因此其直接媒体可获取性仍未知，不能称为已确认的媒体 403 或内容已删除。

## Original pages / 原帖页面

| Case / 案例 | Original page / 原帖 | Result / 结果 |
| --- | --- | --- |
| Bear comparison / 熊对比 | [pixexid](https://x.com/pixexid/status/2118153375464505689) | Accessible without sign-in; both previews shown / 无需登录可打开，显示两张预览 |
| Boxing tiger / 拳击老虎 | [Archiefff](https://x.com/baiji57165/status/2118176730079007145) | Accessible; target MP4 and poster identified / 可打开，已定位目标 MP4 与海报 |
| Hummingbird and kingfisher / 蜂鸟与翠鸟 | [Dheepan Ratnam](https://x.com/Dheepanratnam/status/2118138765487100027) | Accessible; four target MP4s and first poster identified / 可打开，已定位四个目标 MP4 与第一张海报 |
| Rosebud / 玫瑰花苞 | [Michael Guo](https://x.com/Michaelzsguo/status/2118134837357744435) | Accessible; target MP4 identified separately from quoted-post media / 可打开，目标 MP4 与引用帖媒体已区分 |
| Summer mAIfoid / 夏日 mAIfoid | [u/Junior-Grade-2965](https://www.reddit.com/r/mAIfoid/comments/1xo9cd2/a_little_summer_malfoid_animation/) | Reddit network-security block; post content not shown / Reddit 网络安全拦截，未显示帖文内容 |
| Images 2.6 gifts / Images 2.6 礼物 | [u/Algoartist](https://www.reddit.com/r/ChatGPT/comments/1xo6c69/images_26_brings_gifts_d/) | Reddit network-security block; post content not shown / Reddit 网络安全拦截，未显示帖文内容 |

## Nine media requests / 九个媒体地址

Every row below previously returned HTTP 403 to a direct HTTP request. No direct HTTP request was repeated in this recheck. Instead, the visible original post was opened and its actual image/video element was saved normally. The tiger poster was opened at the exact public URL exposed by the video's poster attribute, then saved from the image viewer. No proxy, alternate host, login bypass or security-warning bypass was used.

下表九项此前均为直接 HTTP 请求返回 403。本次未重复该直接请求，而是打开可见原帖，正常保存页面实际图片 / 视频元素。老虎海报从视频 poster 属性提供的准确公开链接打开，再从图片查看页保存。未使用代理、更换主机、绕过登录或绕过安全警告。

| Asset / 素材 | Exact source / 准确来源 | Successful route / 成功路径 | Local file / 仓库文件 |
| --- | --- | --- | --- |
| Bear first preview / 熊第一张预览 | [WebP](https://pbs.twimg.com/media/HWUw0tfaQAAol4Q?format=webp&name=large) | Post image save / 原帖图片保存 | [WebP](../assets/examples/community-bear-svg-comparison/source-01.webp) |
| Tiger animation / 老虎动画 | [MP4](https://video.twimg.com/tweet_video/HWVGfUja0AA4Mww.mp4) | Exact target video save / 目标视频保存 | [MP4](../assets/examples/community-boxing-tiger/source-01.mp4) |
| Tiger poster / 老虎海报 | [WebP](https://pbs.twimg.com/tweet_video_thumb/HWVGfUja0AA4Mww?format=webp&name=large) | Public poster image viewer save / 公开海报图片页保存 | [WebP](../assets/examples/community-boxing-tiger/source-02.webp) |
| Bird variant 1 / 鸟动画 1 | [MP4](https://video.twimg.com/tweet_video/HWUjhD1WoAA4H3e.mp4) | Exact target video save / 目标视频保存 | [MP4](../assets/examples/community-hummingbird-variants/source-01.mp4) |
| Bird variant 2 / 鸟动画 2 | [MP4](https://video.twimg.com/tweet_video/HWUjjV8WEAA1Msj.mp4) | Exact target video save / 目标视频保存 | [MP4](../assets/examples/community-hummingbird-variants/source-02.mp4) |
| Bird variant 3 / 鸟动画 3 | [MP4](https://video.twimg.com/tweet_video/HWUjlaLW0AAZPL5.mp4) | Exact target video save / 目标视频保存 | [MP4](../assets/examples/community-hummingbird-variants/source-03.mp4) |
| Bird variant 4 / 鸟动画 4 | [MP4](https://video.twimg.com/tweet_video/HWUjnGlWsAA1ptO.mp4) | Exact target video save / 目标视频保存 | [MP4](../assets/examples/community-hummingbird-variants/source-04.mp4) |
| First bird poster / 第一张鸟海报 | [WebP](https://pbs.twimg.com/tweet_video_thumb/HWUjhD1WoAA4H3e?format=webp&name=large) | Post image save / 原帖图片保存 | [WebP](../assets/examples/community-hummingbird-variants/source-05.webp) |
| Rose animation / 玫瑰动画 | [MP4](https://video.twimg.com/tweet_video/HWUgYUbWMAAdp79.mp4) | Exact target video save / 目标视频保存 | [MP4](../assets/examples/community-rosebud-animation/source-01.mp4) |

The tiger post contains additional quoted-post media, so its specific video URL was selected rather than the first video on the page. Its transient poster image element disappeared after the video loaded; opening the already observed poster URL provided the normal image-viewer route. These were element-selection issues, not access denials.

老虎原帖还包含引用帖媒体，因此按具体视频 URL 选取，未直接下载页面第一个视频。视频加载后临时海报图片元素消失，改为打开已观察到的海报 URL，在普通图片页保存。这些是元素定位问题，不是访问被拒。

## File verification / 文件核验

- All nine files retain the delivered bytes and exact source URLs; SHA-256, size, actual MIME and creator credits are in `content/source-cases.json`.
- All six MP4s pass full decoding with FFmpeg. Image previews and representative decoded frames were visually checked. This is file verification, not reproduction of the model workflow.
- First two bird clips show hummingbirds beside flowers; last two show kingfishers above water. The case title and media labels were corrected accordingly.
- The creator's “24 fps” description is not presented as measured file data: the four delivered MP4s report 10, 10, about 8.33 and 5.26 fps. This does not establish whether X delivery changed the original timing or how the creator generated/interpolated the animation.
- No MP4 was renamed to GIF; the bear image is a WebP raster preview, not an original SVG. Static posters remain distinct records.
- Independent redistribution licenses remain unverified. Source attribution and the copyright notice do not grant a license.

九个文件均保留实际下载字节与准确来源，并记录校验值、大小、格式和署名。六个 MP4 全量解码通过，已查看图片及代表性视频帧；这不是生成流程复现。已更正蜂鸟 / 翠鸟分类，并将作者自报的 24 fps 与实际 MP4 参数区分。不转换格式，不把 MP4 或静态海报冒充 GIF，转载许可状态保持如实标注。

## Remaining limitation: Reddit / 剩余限制：Reddit

Each exact original URL was opened separately. Both displayed “You've been blocked by network security.” The browser did not expose a numeric HTTP status. No post body or media element was accessible and no verified direct-media URL was available. No direct-media request or download was attempted. This does not establish that the posts or media are unavailable in other authorized browsers.

两个原帖均单独打开，均显示网络安全拦截。浏览器未显示数字 HTTP 状态，未取得帖文、媒体元素或核实的直接素材地址，因此未尝试请求或下载其媒体。此结果不表示帖子或素材在其他获准浏览器中不可用。页面层面已经被拦截，不能据“页面可打开”这一尚未成立的前提推定素材一定能获取。
