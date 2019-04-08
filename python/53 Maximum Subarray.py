class Solution(object):
    def maxSubArray(self, nums):
        res = float('-inf')
        curr = 0
        for i in range(len(nums)):
            curr = max(nums[i], nums[i] + curr)
            res = max(curr, res)
        return res
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
