# Task: for all latest news articles, request its article URL link and retrieve all suggested posts at the bottom of the article page

import requests as req
from bs4 import BeautifulSoup

#use requests to retrieve a website
ms_page=req.get("https://mothership.sg/")
#use beautifulsoup to crawl through the web elements and filter to the latest news articles
ms_soup = BeautifulSoup(ms_page.text, 'html.parser')
latest_news = ms_soup.find('div', id='latest-news')

# Retrieve latest news articles' titles
def title_of_latest_news(article):
    for headlines in article.find_all("div", class_="header"):
        print("\n\n")
        print("Latest news: ")
        print('--------')
        print(headlines.find('h1').text)
        print('--------')
        print("\n")

# Retrieve suggested posts' URL, titles and caption
def suggested_posts_of_latest_news(article):
        for link in article.find_all('a'):
            #request the URL of each of the latest news article
            article_page=req.get(link.get('href'))
            #parse through the texts within the page that the URL brings us to
            ms_art_soup = BeautifulSoup(article_page.text, 'html.parser')
            #filter text by related articles > latest news > ind-article 
            related_news = ms_art_soup.find('div', class_='related-articles')
            for latest_related_article in related_news.find_all('div', id='latest-news'):
                print("Suggested articles for latest news article: ")
                print('--------')
                for related_article in latest_related_article.find_all('div', class_='ind-article'):
                    #print the URL of related articles
                    for related_art_link in related_article.find_all('a'):
                        print(related_art_link.get('href'))
                    #print the header and caption of the related articles
                    for related_post in related_article.find_all("div", class_="container loaded-post-container"):
                        for related_headlines in related_post.find_all('div', class_='header'):
                            print(related_headlines.find('h1').text)
                            print(related_headlines.find('p').text)
                            print('--------')

# For all latest news articles, request its article URL link and retrieve all suggested posts at the bottom of the article page
for article in latest_news.find_all("div", class_="ind-article"):
    title_of_latest_news(article)
    suggested_posts_of_latest_news(article)