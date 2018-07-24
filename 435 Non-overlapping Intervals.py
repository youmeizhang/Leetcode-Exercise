# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        invs = sorted((x.end, x.start) for x in intervals)
        end = -0x7fffffff
        ans = 0
        for e, s in invs:
            if s >= end:
                end = e
                ans += 1
        return len(intervals) - ans
