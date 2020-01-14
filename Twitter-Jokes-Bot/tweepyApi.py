#!/usr/bin/python3.6
# Alternate module for tweet publish
# Incase publish.py does not work

import config
import tweepy

# Authentication to twitter
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

# Api object
api = tweepy.API(auth)

api.update_status("Hello Twitter. Lets see how many Days I can go without getting blocked.. ")