class Solution:
    def findMinArrowShots(self, points):
        emin = 0x7FFFFFFF
        ans = 0
        for s, e in sorted(points):
            if emin < s:
                ans += 1
                emin = 0x7FFFFFFF
            emin = min(emin, e)
        return ans + bool(points)
