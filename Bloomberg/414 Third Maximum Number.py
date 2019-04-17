class Solution(object):
    def thirdMax(self, nums):
        nums = sorted(list(set(nums)), reverse=True)
        if len(nums) < 3:
            return nums[0]
        return nums[2]
        """
        :type nums: List[int]
        :rtype: int
        """
        
