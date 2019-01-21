# news_feed
This parses through several WSJ RSS feeds and creates an audio file out of the article summaries.

You need to install some dependencies fist. 

pip install feedparser

pip install git+https://github.com/DeepHorizons/tts

As you can see we wil use deephorizon tts lib instead of gTTS which has some issues with Python3 and it requires internet connection. deephorizon uses native tts engine. Though it is windows only solution. 
