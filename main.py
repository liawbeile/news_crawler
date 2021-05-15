import requests as req
from bs4 import BeautifulSoup

#use requests
ms_page=req.get("https://mothership.sg/")

ms_soup = BeautifulSoup(ms_page.text, 'html.parser')
# for headline in ms_soup.find_all('h1'):
#     print(headline.text)

# for article in ms_soup.find_all("div", class_="header"):
    # print(article.find('h1').text)
    # print(article.find('p').text)
    # print('-------------')

latest_news = ms_soup.find('div', id='latest-news')

for article in latest_news.find_all("div", class_="ind-article"):
    for link in article.find_all('a'):
        print(link.get('href'))
    for headlines in article.find_all("div", class_="header"):
        print(headlines.find('h1').text)
        print(headlines.find('p').text)
        print('--------')


