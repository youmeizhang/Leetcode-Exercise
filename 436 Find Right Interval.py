# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        ans = []
        invs = sorted((x.start, i) for i, x in enumerate(intervals))
        for x in intervals:
            idx = bisect.bisect_right(invs, (x.end, ))
            if idx < n:
                ans.append(invs[idx][1])
            else:
                ans.append(-1)
        return ans
