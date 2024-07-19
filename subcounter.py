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
        r = requests.get(url=url)
        soup = BeautifulSoup(r.content, features="html.parser")
        x = soup.find_all(name="div")
        for i in x:
            print(i)

if __name__ == "__main__":
    platform = "youtube"
    subcounter(user=USER, platform=platform)
