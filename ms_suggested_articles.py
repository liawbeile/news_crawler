import requests as req
from bs4 import BeautifulSoup

#use requests to retrieve a website
ms_page=req.get("https://mothership.sg/")

#use beautifulsoup to crawl through the web elements
ms_soup = BeautifulSoup(ms_page.text, 'html.parser')

latest_news = ms_soup.find('div', id='latest-news')

for article in latest_news.find_all("div", class_="ind-article"):
    for link in article.find_all('a'):
        article_page=req.get(link.get('href'))
        ms_art_soup = BeautifulSoup(article_page.text, 'html.parser')
        related_news = ms_art_soup.find('div', id='related-articles')
        for latest_related_article in related_news.find_all('div', id='latest-news'):
            for related_article in latest_related_article.find_all('div', class_='ind-article'):
                for related_art_link in related_article.find_all('a'):
                    print(related_art_link.get('href'))
                #for related_post in related_article.find_all("div", class_="container loaded-post-container"):
                for related_headlines in related_post.find_all('div', class_='header'):
                    print(related_headlines.find('h1').text)
                    print(related_headlines.find('p').text)
                    print('--------')

#error, in progress