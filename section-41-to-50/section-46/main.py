from bs4 import BeautifulSoup
import requests

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
date = "2000-08-12"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url=url, headers=headers, verify=False)
# print(response)
soup = BeautifulSoup(response.content, "html.parser")
top_songs = soup.select("h3.c-title.a-no-trucate")
top_artists = soup.select("span.c-label.a-no-trucate")
top_100_songs = []
for i in range(len(top_songs)):
    title = top_songs[i].get_text().strip()
    artist = top_artists[i].get_text().strip()
    top_100_songs.append({'title': title, 'artist': artist})
print(top_100_songs)