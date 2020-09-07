class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort(reverse = True)
        total = 0
        cum = 0
        res = 0
        n = len(satisfaction)
        for i in range(n):
            cum += satisfaction[i]
            cum *= 1
            total += cum
            res = max(res, total)
        return res
            
        
        
