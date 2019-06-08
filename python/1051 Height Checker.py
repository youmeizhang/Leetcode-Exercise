class Solution(object):
    def heightChecker(self, heights):
        tmp = list(sorted(heights))
        res = 0
        n = len(heights)
        for i in range(n):
            if tmp[i] != heights[i]:
                res += 1
        return res
        """
        :type heights: List[int]
        :rtype: int
        """
        
