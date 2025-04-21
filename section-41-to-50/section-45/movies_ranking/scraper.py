from bs4 import BeautifulSoup
import requests

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

requests.packages.urllib3.disable_warnings()
response = requests.get(url = URL, verify=False)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all("h3", class_="title")

output_file = open("movies_ranking.txt", "w", encoding="utf-8")
output_file.write("Ranking\tMovie Name\n")
movies = []
for article in articles:
    text = article.getText().strip()
    # Split 2 parts, before ')' is ranking and after ')' is movie name
    SEPERATOR = ')' if ')' in text else ':'
    parts = text.split(SEPERATOR, 1) 
    ranking = parts[0].strip() 
    movie_name = parts[1].strip() if len(parts) > 1 else ''

    movies.append((ranking, movie_name))
    # print(text)

movies = sorted(movies, key=lambda x: int(x[0]))
for ranking, movie_name in movies:
    output_file.write(f"{ranking}\t{movie_name}\n")
    
output_file.close()