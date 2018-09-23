class Solution:
    def smallestRangeI(self, A, K):
        res = 0
        if len(A) == 1:
            return res
        max_value = max(A)
        min_value = min(A)
        res = max_value - min_value - 2*K 
        return res if res >= 0 else 0
