# credit to: https://leetcode.com/problems/stone-game-ii/discuss/345354/Java-DP-with-memorization-easy-to-understand(with-explanation)

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        if n < 1:
            return 0
        total = [0] * n
        total[-1] = piles[-1]
        for i in range(n-2, -1, -1):
            total[i] = total[i+1] + piles[i]
        
        dp = [[0] * n for _ in range(n)]
        
        def helper(i, M):
            if i == n:
                return 0
            if 2*M >= n - i:
                return total[i]
            if dp[i][M] != 0:
                return dp[i][M]
            min_ = float('inf')
            for x in range(1, 2*M+1):
                min_ = min(min_, helper(i+x, max(M, x)))
            dp[i][M] = total[i] - min_
            return dp[i][M]
        
        return helper(0, 1)
            
        
