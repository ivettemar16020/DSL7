import tweepy
import csv #Import csv
import time
import pandas as pd
import nltk
#nltk.download('stopwords')
from nltk.util import bigrams
from nltk.util import ngrams
from nltk.util import everygrams
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import  re
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

# Open/create a file to append data to
#csvFile = open('result.csv', 'a')
#Use csv writer
#csvWriter = csv.writer(csvFile)

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

fdist_tweets = nltk.FreqDist(filtered_tokens)
#print(fdist_tweets.most_common(20))

#bi_reviews = list(bigrams(filtered_tokens))
#print(bi_reviews)
tri_tweets = list(ngrams(filtered_tokens, n=3))
print(tri_tweets)
