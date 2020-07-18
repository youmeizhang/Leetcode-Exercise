class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n < 3:
            return 0
        dp = [0] * n
        start = 0
        diff = A[1] - A[0]
        res = 0
        for i in range(2, n):
            if A[i] - A[i-1] == diff and i - start + 1 > 2:
                dp[i] = dp[i-1] + 1 + (i+1-start) - 3 
            elif A[i] - A[i-1] != diff:
                res += dp[i-1]
                diff = A[i] - A[i-1]
                start = i - 1
        res += dp[-1]
        return res
            
        
