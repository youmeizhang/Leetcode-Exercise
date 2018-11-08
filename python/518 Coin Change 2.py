class Solution(object):
    def change(self, amount, coins):
        n = amount
        c = coins
        
        if n < 0:
            return 0
        if n == 0:
            return 1
        if c == []:
            return 0

        dp = [[0] * (n+1) for i in range(len(c))]
        for i in range(len(c)):
            dp[i][0] = 1

        for i in range(0, len(c)):
            for j in range(1, n+1):
                if j >= c[i]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-c[i]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(c)-1][n]

class Solution(object):
    def change(self, amount, coins):
        n = amount
        c = coins
        if n == 0:
            return 1
        if c == []:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        for coin in c:
            for i in range(1, n+1):
                if coin <= i:
                    dp[i] += dp[i - coin]
        #print(dp)
        return dp[n]
