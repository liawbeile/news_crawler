# Task: for all latest news articles, request its article URL link and retrieve all suggested posts at the bottom of the article page

import requests as req
from bs4 import BeautifulSoup

#use requests to retrieve a website
ms_page=req.get("https://mothership.sg/")
#use beautifulsoup to crawl through the web elements and filter to the latest news articles
ms_soup = BeautifulSoup(ms_page.text, 'html.parser')
latest_news = ms_soup.find('div', id='latest-news')

# Retrieve latest news articles' titles and captions
def print_headline_and_subtitle(article):
    for headlines in article.find_all("div", class_="header"):
        print(headlines.find('h1').text)
        print(headlines.find('p').text)

# Retrieve suggested posts' URL, titles and caption
def suggested_posts_of_latest_news(article):
    for link in article.find_all('a'):
        article_page=req.get(link.get('href')) #request the URL of each of the latest news article
        ms_art_soup = BeautifulSoup(article_page.text, 'html.parser') #parse through the texts within the page that the URL brings us to
        related_news = ms_art_soup.find('div', class_='related-articles') #filter text by related articles > latest news > ind-article 
        for latest_related_article in related_news.find_all('div', id='latest-news'):
            for related_article in latest_related_article.find_all('div', class_='ind-article'): #print the URL of related articles
                for related_art_link in related_article.find_all('a'):
                    print(related_art_link.get('href'))
                for related_post in related_article.find_all("div", class_="container loaded-post-container"): #print the header and caption of the related articles
                    print_headline_and_subtitle(related_post)
                    print('--------')

# For all latest news articles, request its article URL link and retrieve all suggested posts at the bottom of the article page
def main(latest_news):
    for article in latest_news.find_all("div", class_="ind-article"):
        print("\n\n")
        print("Latest news: ")
        print('--------')
        print_headline_and_subtitle(article)
        print('--------')
        print("\n")
        print("Suggested articles for latest news article: ")
        print('--------')
        suggested_posts_of_latest_news(article)
        
main(latest_news)