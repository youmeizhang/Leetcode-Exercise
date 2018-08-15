class Solution:
    def findRadius(self, houses, heaters):
        m = len(houses)
        n = len(heaters)
        heaters = sorted(heaters)

        ans = 0

        for house in houses:
            tmp = 0x7fffffff
            left = bisect.bisect_right(heaters, house)
            if left > 0:
                tmp = min(tmp, house - heaters[left - 1])
            right = bisect.bisect_left(heaters, house)
            if right < n:
                tmp = min(tmp, heaters[right] - house)
            ans = max(tmp, ans)
        return ans
