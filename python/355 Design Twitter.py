# credit to: https://leetcode.com/problems/design-twitter/discuss/82863/Python-solution


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweet = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)
        self.time = itertools.count(step=-1)
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
       
        self.tweet[userId].appendleft((next(self.time), tweetId))
        
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        timeline = heapq.merge(*(self.tweet[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(timeline, 10)]
            
        
        #return sorted(timeline, key = lambda x:x[1])[:10]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followees[followerId].add(followerId)
        self.followees[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followees[followerId].add(followerId)
        if followerId != followeeId:
            self.followees[followerId].discard(followeeId)
        
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
