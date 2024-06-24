import pandas as pd
import json
import s3fs
from datetime import datetime
import tweepy
import os
import boto3
from botocore.exceptions import NoCredentialsError
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
def twitter_etl():
    tweets_dataset = pd.read_csv("/home/codespace/airflow/twitter_dags/tweets.csv")
    print (tweets_dataset.columns)
    local_file_path = "katyperyy_tweets_data.csv"
    s3_bucket_name = "arjun-twitter-airflow-bucket"
    s3_file_key = "katyperyy_tweets_data.csv"
    katyperry_tweets_dataset = tweets_dataset[tweets_dataset['author'] == 'katyperry']
    katyperry_tweets_dataset.to_csv(local_file_path, index=False)
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file_path, s3_bucket_name, s3_file_key)
        print ("uploaded successfully")
    except FileNotFoundError:

        print ("file not found")
    except NoCredentialsError:
        print ("creds not available")
    # katyperry_tweets_dataset.to_csv("s3://arjun-twitter-airflow-bucket/katyperyy_tweets_data.csv")

# twitter_etl()
