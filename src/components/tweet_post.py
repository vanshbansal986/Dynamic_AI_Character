import tweepy
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_KEY_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

class TweetUpload:
    def __init__(self):
        pass
    
    def v1_endpoint_client(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        
        auth.set_access_token(access_token, access_token_secret)
        
        v1_client = tweepy.API(auth, wait_on_rate_limit=True)

        return v1_client
    
    def v2_endpoint_client(self):
        
        v2_client = tweepy.Client(
            bearer_token,
            consumer_key,
            consumer_secret,
            access_token,
            access_token_secret,
            wait_on_rate_limit=True,
        )

        return v2_client
    
    


    def post_tweet(self ,tweet_type: str , tweet_text:str = "None" , media_path:Path = "None"):
        v1_client = self.v1_endpoint_client()
        v2_client = self.v2_endpoint_client()

        if tweet_type == "text":
            v2_client.create_tweet(text = tweet_text)
            print("✅ Successfully Tweeted ✅")
        elif tweet_type == "image":
            media_id = v1_client.media_upload(filename = media_path).media_id_string

            v2_client.create_tweet(media_ids=[media_id])
            print("✅ Successfully Tweeted ✅")
        elif tweet_type == "image+text":
            media_id = v1_client.media_upload(filename = media_path).media_id_string

            v2_client.create_tweet(text = tweet_text ,media_ids=[media_id])
            print("✅ Successfully Tweeted ✅")




