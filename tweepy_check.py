import tweepy
import pandas as pd


def testCreds():
    try:
        df = pd.read_csv("./keys/twitter_keys.csv")
        # Authenticate to Twitter with read keys
        auth = tweepy.OAuthHandler(df[df['name'] == "ckey"].key.values[0],
                                   df[df['name'] == "csec"].key.values[0])
        auth.set_access_token(df[df['name'] == "atok"].key.values[0],
                              df[df['name'] == "asec"].key.values[0])
        print("Successfully read credentials")
        api = tweepy.API(auth)
        api.verify_credentials()
        public_tweets = api.home_timeline()
        for tweet in public_tweets:
            print(tweet.text)
        print("Tweepy is working\n")
    except Exception as e:
        print(e)
        print("Tweepy is not working\n")


testCreds()
