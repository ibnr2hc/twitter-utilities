import fire
from utilities import client


class Twitter:
    def __init__(self, **kwargs):
        super(Twitter, self).__init__(**kwargs)
        self.client = client.Client()

    def searchUserByFF(self, screen_name, keyword):
        keyword = (keyword,) if not isinstance(keyword, tuple) else keyword
        print("----- Start -----")
        self.client.search.searchUserByFF(screen_name, keyword)
        print("----- Finished -----")


if __name__ == "__main__":
    fire.Fire(Twitter)
