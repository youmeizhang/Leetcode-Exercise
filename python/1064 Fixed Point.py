class Solution(object):
    def fixedPoint(self, A):
        l = 0
        r = len(A) - 1
        res = []
        while l <= r:
            mid = (l + r) // 2
            if A[mid] == mid:
                res.append(mid)
                r = mid - 1
            elif A[mid] < mid:
                l = mid + 1
            else:
                r = mid - 1
        return min(res) if res else -1
        """
        :type A: List[int]
        :rtype: int
        """
