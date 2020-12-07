# Libraries
import json
from tweepy import OAuthHandler, Stream, StreamListener
import configparser
from datetime import datetime
import os

# Reads the credentials file and saves the tokens in variables
config = configparser.ConfigParser()
config.read('./config.ini')
auth_key = config.get('twitter_auth_tokens', "api_key")
auth_secret_key = config.get('twitter_auth_tokens', 'api_secret_key')
access_key = config.get('twitter_access_tokens','api_key')
access_secret_key = config.get('twitter_access_tokens','api_secret_key')

# Defines a file to save the collected tweets
# w = write
today = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
os.makedirs('./02-twitter', exist_ok=True)
out = open(f'./02-twitter/collected_tweets{today}.txt', 'w')

# Implements a class called MyListener() as inheritance from StremListener()
# This class overwrites two methods of StreamListener
class MyListener(StreamListener):
    def on_data(self,data):
        item_string = json.dumps(data)
        out.write(item_string + "\n")
        return True

    def on_error(self,status):
        print(status)

# main
if __name__ == "__main__":
    l = MyListener()
    auth = OAuthHandler(auth_key, auth_secret_key)
    auth.set_access_token(access_key, access_secret_key)

    stream = Stream(auth,l)
    stream.filter(track=['Trump','Biden'])