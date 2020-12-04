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

class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        cost = [[0] * n for _ in range(n)]

        for l in range(2, n+1):
            i = 0
            j = l-1
            while j < n:
                tmp = 0
                if s[i] != s[j]:
                    tmp += 1
                cost[i][j] = tmp + cost[i+1][j-1]
                i += 1
                j += 1

        dp = [[float('inf')] * (k+1) for _ in range(n)]
        for i in range(n):
            dp[i][1] = cost[0][i]
            for q in range(2, k+1):
                for j in range(i):
                    dp[i][q] = min(dp[i][q], dp[j][q-1] + cost[j+1][i])
        return dp[n-1][k]
