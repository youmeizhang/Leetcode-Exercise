class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        res = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
