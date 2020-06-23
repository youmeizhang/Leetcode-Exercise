# refer to: https://leetcode.com/problems/dungeon-game/discuss/698271/Python-Short-DP-7-lines-O(mn)-top-down-explained/588576

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[m-1][n], dp[m][n-1] = 1, 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j], 1)
        return dp[0][0]
