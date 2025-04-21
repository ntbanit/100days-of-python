from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
# print(soup.prettify())
# print(soup.title.string)

all_links = soup.find_all('a')
for link in all_links:
    print(link.get('href'))

heading = soup.find(name='h1', id='name')
print(heading.string)

company_url = soup.select_one(selector='#name')
print(company_url.string)