class Solution(object):
    def numDecodings(self, s):
        if s == "" or s[0] == "0":
            return 0

        def check(char):
            if char[0] == '0':
                return False
            if int(char) > 0 and int(char) <= 26:
                return True
            return False

        n = len(s)
        dp = [0] * n
        dp[0] = 1
        dp[-1] = 1
        for i in range(1, n):
            if check(s[i]) and check(s[i-1] + s[i]):
                dp[i] = dp[i-1] + dp[i-2]
            elif check(s[i]):
                dp[i] = dp[i-1]
            elif check(s[i-1] + s[i]):
                dp[i] = dp[i-2]
            else:
                return 0
        return dp[n-1]
