class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        n = len(timeSeries)
        if n == 0: return 0
        res = 0
        for i in range(1, n):
            diff = timeSeries[i] - timeSeries[i - 1]
            if diff < duration:
                res += diff
            elif diff >= duration:
                res += duration
        return res + duration
