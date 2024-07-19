import os
import dotenv as dv
from pytube import Channel
from instaloader import Instaloader, Profile
from bs4 import BeautifulSoup


def subcounter(user, platform):
    if platform == "youtube":
        url = f"https://youtube.com/channel/{user}"
        channel = Channel(url)
        html = channel.html
        bs = BeautifulSoup(html, "html.parser")
        counter = bs.find_all()
        for x in range(0, len(counter)):
            print(counter[x])
        return counter
    if platform == "instagram":
        L = Instaloader()
        profile = Profile.from_username(L.context, user)
        return profile.followers


if __name__ == "__main__":
    dv.load_dotenv()
    USER = os.getenv("MYUSER")
    platform = "youtube"
    print(subcounter(user=USER, platform=platform))
