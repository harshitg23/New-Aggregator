import requests
from bs4 import BeautifulSoup
# r = requests.get("https://timesofindia.indiatimes.com/briefs")
r = requests.get("https://m.hindustantimes.com/india-news/")
soup = BeautifulSoup(r.content, 'html5lib')
headings = soup.findAll('a')
print(headings)
for h in headings:
    print(h.text)
# headings = soup.find_all('h2')
# headings = headings[0:-13]
# for h in headings:
#     print(h.text)