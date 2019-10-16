import os
import tweepy as tw
import pandas as pd

consumer_key = 'tVXKlrYZ0XtJRhhvMKTIxvuxZ' 
consumer_secret = 'ag5HztuW6fwaHpObEQYw6NXu8dM5J8uwClqonwWX3WnzJnLeJw' 
access_token = '711807286079913985-ugwPIWrPiUCsoWq1DhGGz0PitJ2KeBl' 
access_token_secret = 'KnYNsaiwc5Ow4rk5BE0Pem05RGp7DKXMJPMV68qmHG0EW' 

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#temblor"
date_since = "2019-6-1"

tweets = tw.Cursor(
  api.search,
  q = search_words,
  lang = "es",
  since = date_since
).items(10)


for tweet in tweets:
  print(tweet.text)
  print("////////////////////////")