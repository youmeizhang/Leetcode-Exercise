# credit to: https://leetcode.com/problems/stone-game-ii/discuss/345354/Java-DP-with-memorization-easy-to-understand(with-explanation)
# Min max problem

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
            
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0 for _ in range(n)] for _ in range(n+1)]
        
        def solve(s, M):
            if s >= n:
                return 0
            M = min(n, M)
            if dp[s][M]:
                return dp[s][M]
            if s + 2 * M >= n:
                dp[s][M] = sum(piles[s:])
                return dp[s][M]
            
            best = float('-inf')
            curr = 0
            for x in range(1, 2 * M + 1):
                curr += piles[s+x-1]
                best = max(best, curr - solve(s+x, max(x, M)))
            dp[s][M] = best
            return dp[s][M]
        
        return (sum(piles) + solve(0, 1)) // 2
            
        
