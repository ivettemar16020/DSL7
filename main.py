import tweepy
import csv 
import time
import pandas as pd
import nltk
# nltk.download('stopwords')
from nltk.util import bigrams
from nltk.util import ngrams
from nltk.util import everygrams
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import  re

from matplotlib import pyplot as plt

consumer_key = "0fGnBSc3yWClYpEW1g8fLioQj"
consumer_secret = "uVfnOaKGln5J8XpYVIVMGFj9cgFef2hbgUujtAZYWoItLmw8eG"
access_token = "793556090294198272-puxvkH0l6ZvIj9zyZYQjPTv1dtHLvfc"
access_token_secret = "hcxL5nut6ULHuT65DW48XY3LVD34T7lvQnZ98GSAjNKQ9"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

tweets = tweepy.Cursor(api.search,
                           q = "#TraficoGT  -filter:retweets",
                           since = "2019-10-01",
                           lang = "es").items(1000)

#for tweet in tweets:
#    print(tweet.text)

info = [[tweet.user.screen_name, tweet.user.location, tweet.created_at, tweet.text] for tweet in tweets]
tweet_info = pd.DataFrame(data=info,
                    columns=['user', "location", "created_at", "texto"])
tweet_text = (tweet_info.loc[:, "texto"])
tweet_text = tweet_text.tolist()
tweet_text = ",".join(str(e) for e in tweet_text)
tweet_text = tweet_text.lower()
tweet_text = re.sub(r"http\S+", "", tweet_text)
tokenizer = RegexpTokenizer(r'\w+')

tweet_tokens = tokenizer.tokenize(tweet_text)
#print(tweet_tokens)
stopwords = set(stopwords.words("spanish"))

filtered_tokens = [w for w in tweet_tokens if not w in stopwords]

#fdist_tweets = nltk.FreqDist(filtered_tokens)
#print(fdist_tweets.most_common(20))
#fdist_tweets.plot(30, cumulative=False, title="30 palabras más comúnes")

#bi_reviews = list(bigrams(filtered_tokens))
#print(bi_reviews)
ngrams_list = []
tri_tweets = list(ngrams(filtered_tokens, n=3))
for i, ngram in enumerate(tri_tweets):
    ngram_str = ' '.join(ngram)
    ngrams_list.append(ngram_str)
    #print(ngrams_list[i])


locations = tweet_info.groupby(tweet_info['location']).size().reset_index(name='Count')
print(locations.sort_values(by='Count',ascending=0).head(10))

user_count = tweet_info.groupby(tweet_info['user']).size().reset_index(name='Count')
print(user_count.sort_values(by='Count',ascending=0).head(10))
