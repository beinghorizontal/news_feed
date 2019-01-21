# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 7:32:40 2019

@author: alex1
"""

import feedparser as fp
import shutil
from time import sleep
import tts.sapi

voice = tts.sapi.Sapi()
old_path = 'D:/news_feed/temp/news.mp3'
file_path='D:/news_feed/news.mp3'
feeds = {'moneycontrol': r'http://www.moneycontrol.com/rss/MCtopnews.xml'}
        #'wsj_usb': r'http://www.wsj.com/xml/rss/3_7014.xml',
        #'crypto cointergraph':r'https://cointelegraph.com/editors_pick_rss'}

def news_creator():
    for feed, url in feeds.items():
        parsed = fp.parse(url)
        news = parsed['entries']

        news_sums = []
        for news in news:
            news = news.summary
            news_sums.append(news)
    news_string = ' NEXT STORY. '.join(news_sums)
    print(news_string)

    voice.create_recording('d:/news_feed/temp/news.mp3', news_string)

    shutil.move(old_path, file_path)

"eg. top 3 news" 
top=0
while top<5:
    top+=1
    news_creator()
    print('Created news file.',top)
    sleep(6)

    
