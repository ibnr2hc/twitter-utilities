import tweepy
from .search import Search
import os


CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
CONSUMER_SECRET_KEY = os.environ.get("TWITTER_CONSUMER_SEC_KEY")
ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SEC")


class Client:
    def __init__(self):
        self.client = self._get_client()
        self.search = Search(self.client)

    def _get_client(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        return tweepy.API(auth, wait_on_rate_limit=True)
