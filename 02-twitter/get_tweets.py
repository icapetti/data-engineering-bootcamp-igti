# Libraries
import json
from os import access
from tweepy import OAuthHandler, Stream, StreamListener
import configparser

# Reads the credentials file and saves the tokens in variables
config = configparser.ConfigParser()
config.read('./config.ini')
auth_key = config.get('twitter_auth_tokens', "api_key")
auth_secret_key = config.get('twitter_auth_tokens', 'api_secret_key')
access_key = config.get('twitter_access_tokens','api_key')
access_secret_key = config.get('twitter_access_tokens','api_secret_key')

# Defines a file to save the collected tweets
