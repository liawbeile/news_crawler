# News Crawler  

## News Crawler that can automatically retrieve article links, headlines and subtitles

I am using the Singapore news website, [Mothership](https://mothership.sg/), to create a new crawler, using Requests and BeautifulSoup in Python.  

It is my first attempt at a web automation project using Requests and BeautifulSoup.  

There are 3 files:  
1. In [main.py](https://github.com/liawbeile/news_crawler/blob/main/main.py), I will be practicing how to use requests to retrieve the Mothership website and use beautifulsoup to crawl through the web elements.  
2. In [ms_latest_news.py](https://github.com/liawbeile/news_crawler/blob/main/ms_latest_news.py), I will be retrieving the URL links, header and subtitle of the news articles under the 'Latest News' section of the Mothership website.  
3. In [ms_suggested_articles.py](https://github.com/liawbeile/news_crawler/blob/main/ms_suggested_articles.py), I will be retrieving header and subtitle of all the suggested posts at the bottom of the latest news articles' pages from the 'Latest News' section of the Mothership website.  

I think it's really cool that we can use programming to automate tasks like these for us!