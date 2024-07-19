import os
import dotenv as dv
from pytube import Channel

dv.load_dotenv()
USER = os.getenv("MYUSER")
print(USER)


def subcounter(user, platform):
    if platform == "youtube":
        url = f"https://youtube.com/@{user}"
        channel = Channel(url)
        print(channel)


if __name__ == "__main__":
    platform = "youtube"
    subcounter(user=USER, platform=platform)
