'''In this question we have to design the twitter class'''

from collections import defaultdict

class Twitter:

    def  __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.order = 0


    def postTweet(self,userId,tweetId):
        self.tweets[userId]+= (self.order,tweetId),
        self.order -=1


    def getNewsFeed(self,userId):
        tw = [tw for i in self.following[userId] | {userId} for tw in self.tweets]
        return [news for i,news in tw]

    def follow(self,followerId,followeeId):
        self.following[followeeId].add(followeeId)


    def unfollow(self,followerId,followeeId):
        self.following[followerId].discard(followerId)
        