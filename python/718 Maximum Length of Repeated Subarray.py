class Solution(object):
    def findLength(self, A, B):
        n1 = len(A)
        n2 = len(B)
        res = 0
        
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        
        for i in range(n1):
            for j in range(n2):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res, dp[i][j])       
            
        return res
