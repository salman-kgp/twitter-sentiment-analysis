import tweepy
from ConfigParser import ConfigParser
import sentiment
import sys
from pprint import pprint

CONFIG_FILE="config.ini"

config=ConfigParser()
config.read(CONFIG_FILE)

consumer_key=config.get("consumer","key")
consumer_secret=config.get("consumer","secret")

access_tocken=config.get("access","tocken")
access_secret=config.get("access","secret")

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_tocken,access_secret)


api=tweepy.API(auth)

search_key=sys.argv[1]

tweets=api.search(search_key)

for tw in tweets:
	pprint(tw.text)
	pprint(sentiment.get_sentiment(tw.text))



