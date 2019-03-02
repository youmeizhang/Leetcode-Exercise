# Credit to: https://blog.csdn.net/yurenguowang/article/details/76665171
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        if intervals == []:
            return 0
        
        tmp = []
        for inter in intervals:
            tmp.append([inter.start, True])
            tmp.append([inter.end, False])
        tmp = sorted(tmp, key = lambda x:(x[0], x[1]))
        n = 0
        max_num = 0
        for arr in tmp:
            if arr[1]:
                n += 1
            else:
                n -= 1
            max_num = max(n, max_num)
        return max_num
    
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
