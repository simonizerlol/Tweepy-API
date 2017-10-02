import tweepy
from tweepy import OAuthHandler

consumer_key='XXXX'
consumer_secret='XXXX'
access_token='XXX-XXXX'
access_secret='XXXX'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# print status
for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)

# post status
api.update_status("Hello World!")

# update profile pic
api.update_profile_image("abc.jpg")

#for more check documentation: http://docs.tweepy.org/en/v3.5.0/