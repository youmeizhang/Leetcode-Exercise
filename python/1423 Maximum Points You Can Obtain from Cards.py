# credit to: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/discuss/812818/Explained-DP-%2B-Window-Sliding-or-C%2B%2B

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total= sum(cardPoints)
        n = len(cardPoints)
        i = 0
        s = 0
        while i < n-k:
            s += cardPoints[i]
            i += 1
            
        res = 0
        res = max(res, total - s)
        
        while i < n:
            s -= cardPoints[i-(n-k)]
            s += cardPoints[i]
            res = max(res, total - s)
            i += 1
        return res
        

class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        if k >= n:
            return sum(cardPoints)
        
        dp = [[0] * n for _ in range(n)]

        
        def go(s, e, cardPoints, k):
            if k == 0:
                return 0
            
            if dp[s][e] == -1:
                return dp[s][e]
            
            dp[s][e] = max(go(s+1, e, cardPoints, k-1) + cardPoints[s], go(s, e-1, cardPoints, k-1) + cardPoints[e])
            
            return dp[s][e]
        
        return go(0, n-1, cardPoints, k)

                
