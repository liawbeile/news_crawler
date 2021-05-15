import requests as req
from bs4 import BeautifulSoup

#use requests to retrieve a website
ms_page=req.get("https://mothership.sg/")

#use beautifulsoup to crawl through the web elements
ms_soup = BeautifulSoup(ms_page.text, 'html.parser')

latest_news = ms_soup.find('div', id='latest-news')

for article in latest_news.find_all("div", class_="ind-article"):
    for link in article.find_all('a'):
        print(link.get('href'))
    for headlines in article.find_all("div", class_="header"):
        print(headlines.find('h1').text)
        print(headlines.find('p').text)
        print('--------')