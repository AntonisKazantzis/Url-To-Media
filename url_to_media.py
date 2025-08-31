import argparse
from pathlib import Path
import yt_dlp
import os

def get_default_download_dir():
    return Path(os.path.expanduser("~/Downloads"))

def build_opts(outdir: Path, target_format: str):
    outtmpl = str(outdir / "%(title)s.%(ext)s")

    if target_format.lower() == "mp3":
        return {
            "outtmpl": outtmpl,
            "noplaylist": True,
            "format": "bestaudio/best",
            "postprocessors": [
                {"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "320"},
                {"key": "FFmpegMetadata"},
            ],
        }

    return {
        "outtmpl": outtmpl,
        "noplaylist": True,
        "format": (
            "bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/"
            "best[ext=mp4][height<=1080]/"
            "bestvideo[height<=1080]+bestaudio/"
            "best"
        ),
        "merge_output_format": "mp4",
        "postprocessors": [{"key": "FFmpegMetadata"}],
    }

def main():
    parser = argparse.ArgumentParser(description="Download one or more URLs as MP3 (320 kbps) or MP4 (up to 1080p).")
    parser.add_argument("urls", nargs='+', help="One or more video/audio URLs")
    parser.add_argument("--format", "-f", default="mp4", choices=["mp3", "mp4"], help="Output format")
    parser.add_argument(
        "--outdir", "-o",
        default=get_default_download_dir(),
        help="Output directory (default: system Downloads folder)"
    )
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    ydl_opts = build_opts(outdir, args.format)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(args.urls)  # download all URLs at once

if __name__ == "__main__":
    main()
