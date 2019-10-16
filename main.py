import tweepy
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