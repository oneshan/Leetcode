#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter
#
# Medium (25.15%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user and is able to see the 10 most recent tweets in
# the user's news feed. Your design should support the following methods:
#
#
#
# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news
# feed. Each item in the news feed must be posted by users who the user
# followed or by the user herself. Tweets must be ordered from most recent to
# least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
#
#
#
# Example:
#
# Twitter twitter = new Twitter();
#
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
#
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
#
# // User 1 follows user 2.
# twitter.follow(1, 2);
#
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
#
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id
# 5.
# twitter.getNewsFeed(1);
#
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
#
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);
#
#
#
import heapq


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._tweets = {}
        self._following = {}
        self._time = 0
        self._feedsize = 10

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self._time += 1
        self._tweets.setdefault(userId, [])
        self._tweets[userId].append((self._time, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        userList = [userId] + list(self._following.get(userId, []))
        maxheap = []
        for user in userList:
            if user in self._tweets:
                time = self._tweets[user][-1][0]
                heapq.heappush(maxheap, (-time, user, 1))

        result = []
        for _ in range(self._feedsize):
            if not maxheap:
                break
            time, user, idx = heapq.heappop(maxheap)
            result.append(self._tweets[user][-idx][1])
            idx += 1
            if idx <= len(self._tweets[user]):
                time = self._tweets[user][-idx][0]
                heapq.heappush(maxheap, (-time, user, idx))
        return result

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        self._following.setdefault(followerId, set())
        self._following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        if followerId in self._following:
            self._following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
if __name__ == "__main__":
    twitter = Twitter()
    posts = [
        [2, 5],
        [1, 3],
        [1, 101],
        [2, 13],
        [2, 10],
        [1, 2],
        [2, 94],
        [2, 505],
        [1, 333],
        [1, 22]
    ]
    for userId, tweetId in posts:
        twitter.postTweet(userId, tweetId)
    assert(twitter.getNewsFeed(2) == [505, 94, 10, 13, 5])
    twitter.follow(2, 1)
    assert(twitter.getNewsFeed(2) == [22, 333, 505, 94, 2, 10, 13, 101, 3, 5])

    twitter = Twitter()
    twitter.postTweet(1, 5)
    assert(twitter.getNewsFeed(1) == [5])
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert(twitter.getNewsFeed(1) == [6, 5])
    twitter.unfollow(1, 2)
    assert(twitter.getNewsFeed(1) == [5])
