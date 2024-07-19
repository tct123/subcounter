from bs4 import BeautifulSoup
import os
import dotenv as dv
import requests

dv.load_dotenv()
USER = os.getenv("MYUSER")
print(USER)


def subcounter(user, platform):
    if platform == "youtube":
        url = f"https://youtube.com/@{user}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }
        r = requests.get(url, headers)
        soup = BeautifulSoup(r.content, "html.parser")
        x = soup.find(
            {"id": "subscriber-count"}, name="yt-formatted-string"
        ).text.strip()
        print()


if __name__ == "__main__":
    platform = "youtube"
    subcounter(user=USER, platform=platform)
