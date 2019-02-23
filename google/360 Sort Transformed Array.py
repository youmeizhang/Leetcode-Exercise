class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        return sorted([(i ** 2) * a + b * i + c for i in nums])
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        
