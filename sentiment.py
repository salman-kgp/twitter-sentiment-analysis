from textblob import TextBlob
import re


def preprocess(tweet):
	return " ".join(re.findall("[A-Za-z]+",tweet))

def get_sentiment(tweet):
	tweet_blob=TextBlob(preprocess(tweet))
	return tweet_blob.sentiment