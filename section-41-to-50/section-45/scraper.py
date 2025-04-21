from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news", verify=False)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all("span", class_="titleline")
article_text = []
article_links = []
article_score = []

for article_tag in articles:
    text = article_tag.getText()
    article_text.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

response_score = soup.find_all("span", class_="score")
article_score = [int(scores.getText().strip(" points")) for scores in response_score]

highest_score = max(article_score)
highest_index = article_score.index(highest_score)


print(
    f"Most upvoted article: {article_text[highest_index]}\n"
    f"Number of upvotes: {article_score[highest_index]} points\n"
    f"Available at: {article_links[highest_index]}"
)