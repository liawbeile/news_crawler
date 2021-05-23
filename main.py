import requests as req
from bs4 import BeautifulSoup

#use requests to retrieve a website
ms_page=req.get("https://mothership.sg/")

#use beautifulsoup to crawl through the web elements
ms_soup = BeautifulSoup(ms_page.text, 'html.parser')
for headline in ms_soup.find_all('h1'):
    print(headline.text)

for article in ms_soup.find_all("div", class_="header"):
    print(article.find('h1').text)
    print(article.find('p').text)
    print('-------------')