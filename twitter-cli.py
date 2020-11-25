import fire
from utilities import client


class Twitter:
    def __init__(self, **kwargs):
        super(Twitter, self).__init__(**kwargs)
        self.client = client.Client()

    def searchUserByFF(self, screen_name, keyword):
        print("----- Start -----")
        users = self.client.search.searchUserByFF(screen_name, keyword)
        
        if users:
            print(f"Hit user by {keyword}\n\n")
        for user in users:
            print(f"- {user['name']} (@{user['screen_name']})")

        print("----- Finished -----")


if __name__ == "__main__":
    fire.Fire(Twitter)
