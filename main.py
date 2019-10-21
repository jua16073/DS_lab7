import os
import tweepy as tw
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('spanish'))

consumer_key = 'tVXKlrYZ0XtJRhhvMKTIxvuxZ' 
consumer_secret = 'ag5HztuW6fwaHpObEQYw6NXu8dM5J8uwClqonwWX3WnzJnLeJw' 
access_token = '711807286079913985-ugwPIWrPiUCsoWq1DhGGz0PitJ2KeBl' 
access_token_secret = 'KnYNsaiwc5Ow4rk5BE0Pem05RGp7DKXMJPMV68qmHG0EW' 

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#temblorgt"
date_since = "2019-6-1"

tweets = tw.Cursor(
  api.search,
  q = search_words,
  lang = "es",
  since = date_since
).pages(1000)

new_data = []

for page in tweets:
  for tweet in page:
    tweet.text = tweet.text.lower()
    important = []
    words = tweet.text.split(" ")
    for word in words:
      if word not in stop_words:
        word = word.replace('á', 'a')
        word = word.replace('é', 'e')
        word = word.replace('í', 'i')
        word = word.replace('ó', 'o')
        word = word.replace('ú', 'u')
        word = word.replace('ñ', 'n')
        word = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",word).split())
        important.append(word)
    new_data.append(important)

strings = []
for t in new_data:
  string = ""
  for word in t:
    string = string + word + " "
  strings.append(string)

file = open('data.txt', "w+")
for t in strings:
  file.write(t + ';')
file.close()
