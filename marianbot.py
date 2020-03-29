import tweepy
import os
import datetime

today = datetime.date.today()
someday = datetime.date(2020, 3, 29) # The day marianb0t was born
diff = someday - today

# Authenticate to Twitter
auth = tweepy.OAuthHandler(os.environ["TWITTER_CONSUMER_KEY"], os.environ["TWITTER_CONSUMER_SECRET"])
auth.set_access_token(os.environ["TWITTER_ACCESS_TOKEN_KEY"], os.environ["TWITTER_ACCESS_TOKEN_SECRET"])

# Create API object
api = tweepy.API(auth)

# Create a tweet
# https://twitter.com/twitterdev/status/977224051419766786

tweet = (os.getenv('TWITTER_MSG', 'YES')) + " #dailymarianday" + str(diff.days) 
api.update_status(tweet)