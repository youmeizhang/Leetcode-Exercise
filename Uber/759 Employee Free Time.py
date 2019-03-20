# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def employeeFreeTime(self, schedule):
        intervals = schedule[0]
        n = len(schedule)
        for i in range(1, n):
            for inter in schedule[i]:
                intervals.append(inter)

            intervals = sorted(intervals, key=lambda x: x.start)
            res = [intervals[0]]

            for j in range(1, len(intervals)):
                if res[-1].end > intervals[j].start:
                    res[-1].end = max(res[-1].end, intervals[j].end)
                else:
                    res.append(intervals[j])

        ans = []
        for i in range(1, len(res)):
            if res[i].start> res[i-1].end:
                ans.append([res[i-1].end, res[i].start])

        return ans
                
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        
