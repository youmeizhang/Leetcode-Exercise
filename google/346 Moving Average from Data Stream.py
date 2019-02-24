class MovingAverage(object):

    def __init__(self, size):
        self.winsize = size
        self.l = []
        """
        Initialize your data structure here.
        :type size: int
        """
        

    def next(self, val):
        self.l.append(val)
        if len(self.l) < self.winsize:
            return sum(self.l) / float(len(self.l))
        return sum(self.l[-1 * self.winsize:]) / float(self.winsize)
        """
        :type val: int
        :rtype: float
        """
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
