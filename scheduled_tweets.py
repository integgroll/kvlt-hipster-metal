import tweepy
import os
import random 

CONSUMER_API = os.environ["CONSUMER_API_KEY"]
CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(CONSUMER_API, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

tweets = ["I'm a bad bot. Please alert my mistress, @ComradeEevee when I do something like tweet something pro-nsbm. FUCK THE PANDA COSPLAYERS!!!", "Your regularly scheduled reminder: FUCK NSBM! BE GAY, DO CRIME! THE BLACK METAL SCENE MUST BE DESTROYED!", "any ideas on how i can be a better bot? want to see some automated metal shitposting? dm me or @ComradeEevee"]

tweet = random.choice(tweets)
print(f"scheduled tweet: {tweet}")
api.update_status(tweet)


