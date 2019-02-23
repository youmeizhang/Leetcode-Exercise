# time limit

class RangeModule(object):

    def __init__(self):
        self.ranges = []

    def addRange(self, left, right):

        if self.ranges == []:
            self.ranges.append([left, right])
        else:
            
            self.ranges.append([left, right])
            self.ranges = sorted(self.ranges, key = lambda x : x[0])
            res = [self.ranges[0]]

            for i in range(1, len(self.ranges)):
                if res[-1][1] >= self.ranges[i][0]:
                    res[-1][1] = max(res[-1][1], self.ranges[i][1])
                else:
                    res.append(self.ranges[i])
            self.ranges = copy.deepcopy(res)        

    def queryRange(self, left, right):
        r = len(self.ranges) - 1
        l = 0
        while(l <= r):
            mid = (l + r) // 2
            if self.ranges[mid][0] <= left and self.ranges[mid][1] >= right:
                return True
            elif self.ranges[mid][1] < left:
                l = mid + 1
            else:
                r = mid - 1
        return False
        

    def removeRange(self, left, right):
        
        n = len(self.ranges)
        tmp = []
        for i in range(n):
            if self.ranges[i][1] <= left or self.ranges[i][0] >= right:
                tmp.append(self.ranges[i])
            else:
                if self.ranges[i][0] < left:
                    tmp.append([self.ranges[i][0], left])
                if self.ranges[i][1] > right:
                    tmp.append([right, self.ranges[i][1]])
                
        self.ranges = copy.deepcopy(tmp)
