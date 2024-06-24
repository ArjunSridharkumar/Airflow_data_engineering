import pandas as pd
import json
import s3fs
from datetime import datetime
import tweepy
import os
# twitter_key = os.environ['TWITTER_API_KEY']
# twitter_key_secret = os.environ['TWITTER_API_KEY_SECRET']
# twitter_access_key = os.environ['TWITTER_ACCESS_KEY']
# twitter_access_key_secret = os.environ['TWITTER_ACCESS_KEY_SECRET']
# # print (twitter_key,twitter_key_secret,twitter_access_key,twitter_access_key_secret)

# #Twitter Auth
# auth = tweepy.OAuthHandler(twitter_key,twitter_key_secret)
# auth.set_access_token(twitter_access_key,twitter_access_key_secret)
# api = tweepy.API(auth)

# api.user_timeline(screen_name = "@elonmusk",
#                   count = 200,
#                   include_rts = False,
#                   tweet_model = "extended")

# print (tweets)

tweets_dataset = pd.read_csv("tweets.csv")
print (tweets_dataset.columns)
katyperry_tweets_dataset = tweets_dataset[tweets_dataset['author'] == 'katyperry']

