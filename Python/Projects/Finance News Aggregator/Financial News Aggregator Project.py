from pprint import pprint 
from finnews.client import News

news_client = News()

cnbc_news_client = news_client.cnbc

cnbc_top_news = cnbc_news_client.news_feed(topic='top_news')

pprint(cnbc_top_news)