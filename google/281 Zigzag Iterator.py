class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.vl1 = v1
        self.vl2 = v2
        self.v1start = 0
        self.v2start = 0
        self.count = 0
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        

    def next(self):
        if self.count % 2 == 0 and self.v1start < len(self.vl1):
            self.v1start += 1
            self.count += 1
            return self.vl1[self.v1start - 1]
        elif self.count % 2 == 1 and self.v2start < len(self.vl2):
            self.v2start += 1
            self.count += 1
            return self.vl2[self.v2start - 1]
        elif self.v1start < len(self.vl1):
            self.v1start += 1
            return self.vl1[self.v1start - 1]
        elif self.v2start < len(self.vl2):
            self.v2start += 1
            return self.vl2[self.v2start - 1]
        else:
            return None
        
        """
        :rtype: int
        """
        

    def hasNext(self):
        if self.v1start < len(self.vl1) or self.v2start < len(self.vl2):
            return True
        return False
            
        """
        :rtype: bool
        """
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
