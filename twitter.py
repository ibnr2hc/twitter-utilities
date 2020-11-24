import fire


class Twitter:
    def searchUserByFF(self, screen_name, keyword):
        print("screen_name: ", screen_name)
        print("keyword: ", keyword)


if __name__ == "__main__":
    fire.Fire(Twitter)
