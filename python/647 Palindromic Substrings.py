class Solution:
    def countSubstrings(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(i):
                dp[j][i] = (s[i] == s[j]) and ((i - j < 2) or dp[j+1][i-1])

                if dp[j][i]:
                    count += 1
            dp[i][i] = 1
            count += 1


        return count
