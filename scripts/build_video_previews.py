#!/usr/bin/env python3
"""从主合集原始 MP4 提取 README 首帧，原视频保持不变。需要 ffmpeg。"""
import argparse
import subprocess
from common import ROOT
from source_cases import read_cases, video_preview_path, visible


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='只检查预览文件是否存在')
    args = parser.parse_args()
    count = 0
    for item in visible(read_cases()):
        for media in item['media']:
            if media['kind'] != 'video' or not media['path']:
                continue
            target = ROOT / video_preview_path(media)
            if args.check:
                if not target.is_file() or not target.stat().st_size:
                    raise SystemExit(f'缺少视频首帧：{target.relative_to(ROOT)}')
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', str(ROOT / media['path']),
                                '-frames:v', '1', '-vf', "scale='min(640,iw)':-2", '-q:v', '3', str(target)], check=True)
            count += 1
    print(f'已{"检查" if args.check else "生成"} {count} 张视频首帧；来源 MP4 保持原样。')


if __name__ == '__main__':
    main()
