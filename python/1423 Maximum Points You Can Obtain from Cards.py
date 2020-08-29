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

                
