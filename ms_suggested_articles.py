import requests as req
from bs4 import BeautifulSoup

#use requests to retrieve a website
ms_page=req.get("https://mothership.sg/")

#use beautifulsoup to crawl through the web elements and filter to the latest news articles
ms_soup = BeautifulSoup(ms_page.text, 'html.parser')
latest_news = ms_soup.find('div', id='latest-news')

#for all latest news articles, request its article URL link and retrieve all suggested posts at the bottom of the article page
def suggested_posts_of_latest_news(latest_news):
    for article in latest_news.find_all("div", class_="ind-article"):
        for headlines in article.find_all("div", class_="header"):
            print("\n")
            print("Suggested articles for article titled: " + headlines.find('h1').text)
            print('--------')
        for link in article.find_all('a'):
            #request the URL of each of the latest news article
            article_page=req.get(link.get('href'))
            #parse through the texts within the page that the URL brings us to
            ms_art_soup = BeautifulSoup(article_page.text, 'html.parser')
            #filter text by related articles > latest news > ind-article 
            related_news = ms_art_soup.find('div', class_='related-articles')
            for latest_related_article in related_news.find_all('div', id='latest-news'):
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

suggested_posts_of_latest_news(latest_news)