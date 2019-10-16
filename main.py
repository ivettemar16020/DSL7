import tweepy
import csv #Import csv
import time
import pandas as pd


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
                           since = "2018-01-01",
                           until = "2018-12-31",
                           lang = "en").items(10)

    # Write a row to the CSV file. I use encode UTF-8
    #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    #print (tweet.created_at, tweet.text)


info = [[tweet.user.screen_name, tweet.user.location, tweet.created_at, tweet.text] for tweet in tweets]

tweet_info = pd.DataFrame(data=info, 
                    columns=['user', "location", "created_at", "texto"])
print(tweet_info)

#csvFile.close()