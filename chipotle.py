import tweepy


consumer_key = "XXXXXXXXX"
consumer_secret = "XXXXXXXXX"
access_token = "XXXXXXXXX"
access_token_secret = "XXXXXXXXX"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

