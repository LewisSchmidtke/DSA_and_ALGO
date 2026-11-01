import heapq
from typing import List
from dataclasses import dataclass


class Twitter:

    def __init__(self):
        self.twitter: dict[int, UserData] = {}
        self.recent_id = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self._get_or_create_user(userId)
        user.tweets.append((self.recent_id, tweetId))
        self.recent_id += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.twitter:
            return []

        all_tweets = []
        for followee_id in self.twitter[userId].following:
            if followee_id not in self.twitter:
                continue

            # Only 10 most recent tweets per follower
            all_tweets.extend(self.twitter[followee_id].tweets[-10:])

        # Take the total 10 newest tweets from all users the user_id is following
        newest = heapq.nlargest(10, all_tweets)
        return [tweet_id for _, tweet_id in newest]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        user = self._get_or_create_user(followerId)
        user.following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:  # Prevent unfollowing themselves
            return

        if followerId in self.twitter:
            self.twitter[followerId].following.discard(followeeId)

    def _get_or_create_user(self, user_id: int) -> UserData:
        """Returns UserData from specific user_id if it exists, otherwise creates new user."""
        if user_id not in self.twitter:
            self.twitter[user_id] = UserData(
                following={user_id},
                tweets=[]
            )

        return self.twitter[user_id]
        
        
@dataclass
class UserData:
    following: set[int]
    tweets: list[tuple[int, int]]
    