class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        if n <= k:
            return 0
        
        def minChanges(i, j):
            res = 0
            while i < j:
                if s[i] != s[j]:
                    res += 1
                i += 1
                j -= 1
            return res

        dp = [[float('inf')] * (k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][1] = minChanges(0, i-1)
            for q in range(1, k+1):
                for j in range(1, i):
                    dp[i][q] = min(dp[i][q], dp[j][q-1] + minChanges(j, i-1))
        return dp[n][k]
