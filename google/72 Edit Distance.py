class Solution(object):
    def minDistance(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0] * (l1+1) for _ in range((l2+1))]
        for i in range(1, l1 + 1):
            dp[0][i] = i

        for j in range(1, l2 + 1):
            dp[j][0] = j

        for j in range(1, l2 + 1):
            for i in range(1, l1 + 1):
                if word1[i-1] != word2[j-1]:
                    dp[j][i] = min(dp[j-1][i], dp[j][i-1], dp[j-1][i-1]) + 1
                else:
                    dp[j][i] = dp[j-1][i-1]
        return dp[l2][l1]
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
