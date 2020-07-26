# credit to: https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-1155-number-of-dice-rolls-with-target-sum/

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (target+1) for _ in range(d+1)]
        dp[0][0] = 1 
        for i in range(1, d+1):
            for j in range(1, f+1):
                for t in range(j, target+1):
                    dp[i][t] = (dp[i][t] + dp[i-1][t-j]) % mod
        print(dp)
        return dp[d][target]
    

