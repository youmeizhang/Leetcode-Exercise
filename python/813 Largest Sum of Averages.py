class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        total = [0] * (n+1)
        dp = [[0] * (n+1) for _ in range(K+1)]
        for i in range(1, n+1):
            total[i] = total[i-1] + A[i-1]
            dp[1][i] = total[i] / i
        
        for k in range(2, K+1):
            for i in range(k, n+1):
                for j in range(k-1, i):
                    dp[k][i] = max(dp[k][i], dp[k-1][j] + (total[i] - total[j]) / (i - j))
        return dp[K][n]
