# Basic idea:
# For each number as a root, we calculate the posibility of left part and right part combination and then multiply them
# For DP idea, example [1,2,3,4,5,6,7] if we choose 3 as the root, then the possibility of left part can be considered as dp[2] and the right part can be like dp[4] 
class Solution(object):
    def numTrees(self, n):
        g = [0] * (n+1)
        g[0], g[1] = 1, 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                g[i] += g[i-j] * g[j-1]
                
        return g[n]
        """
        :type n: int
        :rtype: int
        """
