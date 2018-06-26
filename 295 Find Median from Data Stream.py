class MedianFinder(object):

    def __init__(self):
        self.small = []
        self.large = []
        """
        initialize your data structure here.
        """
        

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        """
        :type num: int
        :rtype: void
        """
        

    def findMedian(self):
        if len(self.small) == len(self.large):
            median = float(self.large[0] - self.small[0]) / 2.0
        else:
            median = float(self.large[0])
        return median
