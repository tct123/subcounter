import yt_dlp
import os
import dotenv as dv
import requests

dv.load_dotenv()
USER = os.getenv("MYUSER")
print(USER)

# URL des YouTube-Kanals
url = f"https://youtube.com/@{USER}/about"
ydl_opts = {
    "quiet": True,
    "force_generic_extractor": True,
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url, download=False)
    print(f"Channel Title: {info['title']}")
    print(f"Channel Description: {info.get('description', 'No description available')}")
    print(f"Subscribers: {info.get('subscriber_count', 'N/A')}")
    print(f"Total Videos: {len(info['entries'])}")
    info.get()
