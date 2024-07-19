import os
import dotenv as dv
from pytube import Channel
from instaloader import Instaloader, Profile


def subcounter(user, platform):
    if platform == "youtube":
        url = f"https://youtube.com/c/{user}"
        channel = Channel(url)
        channel.channel_name
    if platform == "instagram":
        L = Instaloader()
        profile = Profile.from_username(L.context, user)
        print(profile.followers)


if __name__ == "__main__":
    dv.load_dotenv()
    USER = os.getenv("MYUSER")
    platform = "instagram"
    subcounter(user=USER, platform=platform)
