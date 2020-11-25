import tweepy


class Search:
    def __init__(self, client):
        self.client = client

    def searchUserByFF(self, screen_name, keyword):
        """Keywordに合致するフォローフォロワー情報を取得する
    
        Args:
            screen_name(string): 検索するユーザー
            keyword(string): 検索するキーワード
    
        Returns:
            users(list): キーワードに合致するフォロー・フォロワー
        """
        # TODO: screen_nameからユーザーを取得する
        # TODO: screen_nameに合致するユーザーでない場合は例外を送出する
        ffs = []
        for follower in tweepy.Cursor(self.client.followers, screen_name=screen_name).items():
            ffs.append({
                "screen_name": follower.screen_name,
                "description": follower.description,
                "name": follower.name
            })

        # フォローしている人を一覧をリストに入れる
        # TODO: フォローフォロワーの一覧をリストに入れる
        # TODO: 重複するユーザーは多重でリストに入らないようにする
        hit_users = []
        for follower in ffs:
            if self._is_compare(follower, keyword.lower()):
                hit_users.append({
                    "screen_name": follower["screen_name"],
                    "name": follower["name"]
                })

        return hit_users


    def _is_compare(self, user, keyword):
        """Keywordがscreen_name, description, nameのいずれかと部分一致した場合はTrueを返す
        """
        if keyword in str(user["screen_name"]).lower():
            return True
        if keyword in str(user["description"]).lower():
            return True
        if keyword in str(user["name"]).lower():
            return True

