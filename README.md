# 🎵 URL to Media Downloader

A lightweight Python tool to download videos or audio from URLs (e.g. YouTube) with multiple features:

- **MP3 @ 320 kbps** (high-quality audio)  
- **MP4 up to 1080p** (video with audio merged)  
- **Multiple URLs in one command**  
- **Default output to your system Downloads folder**  
- Powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp) + [FFmpeg](https://ffmpeg.org)  

---

## 🚀 Features
- 🎧 Extract **MP3 (320 kbps)** with proper metadata  
- 🎬 Download **MP4 videos up to 1080p** with audio merged  
- 🔗 Accepts **multiple URLs** in a single run  
- 💾 Saves files directly to your **Downloads folder** by default  
- 🌍 Works with **hundreds of websites** supported by `yt-dlp`  
- 🪶 Lightweight: just Python + free tools  

---

## 📥 Installation

### 1. Clone Repository
```bash
git clone https://github.com/AntonisKazantzis/url-to-media.git
cd url-to-media
```

---

## ▶️ Usage

### 1. Run Rcript
```bash
python url_to_media.py "--> MEDIA URL HERE <--" --format mp4
```