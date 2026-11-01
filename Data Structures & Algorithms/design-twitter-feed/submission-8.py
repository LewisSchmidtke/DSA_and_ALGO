from dataclasses import dataclass
class Twitter:

    def __init__(self):
        self.twitter = {}
        self.recent_id = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.twitter:
            new_user = UserData(userId, {userId}, [(self.recent_id, tweetId)])
            self.twitter[userId] = new_user
        else:
            self.twitter[userId].tweets.append((self.recent_id, tweetId))

        self.recent_id += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.twitter:
            return []

        all_tweets = []

        for followerId in self.twitter[userId].following:
            tweets = self.twitter[followerId].tweets
            if not tweets:
                continue
            if len(tweets) >= 10:
                all_tweets.extend(tweets[-10:])
            else:
                all_tweets.extend(tweets)

        res = []
        heapq.heapify_max(all_tweets)
        for k in range(10):
            if not all_tweets:
                break
            res.append(heapq.heappop_max(all_tweets))

        cleaned = [t_Id for _, t_Id in res]
        return cleaned
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.twitter:
            new_user = UserData(followerId, {followerId, followeeId}, [])
            self.twitter[followerId] = new_user
        else:
            self.twitter[followerId].following.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.twitter and followeeId in self.twitter[followerId].following:
            self.twitter[followerId].following.remove(followeeId)
        
@dataclass
class UserData:
    userID : int
    following : set
    tweets : list[int]
    