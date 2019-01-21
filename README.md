# news_feed
This parses through several WSJ RSS feeds and creates an audio file out of the article summaries.

You need to install some dependencies fist. 

pip install feedparser

pip install git+https://github.com/DeepHorizons/tts

As you can see we will use deephorizon tts lib instead of gTTS which have some issues with Python3 and it requires an internet connection. Deephorizon uses native tts engine, it is fast as tts conversion will be local. Though it is windows only solution. 

I have included rss feed for Moneycontrol, WSJ and cryptocurrency rss feed from cointelegraph. Uncomment the one which you intend to use. 

