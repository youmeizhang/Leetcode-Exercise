class HitCounter(object):

    def __init__(self):
        self.l = []
        """
        Initialize your data structure here.
        """
        

    def hit(self, timestamp):
        self.l.append(timestamp)
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        

    def getHits(self, timestamp):
        val = timestamp - 60 * 5
        
        count = 0
        #larger than this and smaller than timestamp
        for i in range(len(self.l)):
            if self.l[i] > val and self.l[i] <= timestamp:
                count += 1

        return count
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
