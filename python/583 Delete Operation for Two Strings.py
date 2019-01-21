class Solution(object):
    def minDistance(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)
        res = 0

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1):
            for j in range(n2):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        for i in range(n1 + 1):
            res = max(res, max(dp[i]))

        return n1 - res + n2 - res
