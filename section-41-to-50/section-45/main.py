from bs4 import BeautifulSoup
import requests

requests.packages.urllib3.disable_warnings()
response = requests.get(url="https://appbrewery.github.io/news.ycombinator.com/", verify=False)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all('a', class_='storylink')
for article in articles:
    title = article.get_text()
    link = article.get('href')
    print(f"Title: {title}")
    print(f"Link: {link}")
    print("-" * 80)