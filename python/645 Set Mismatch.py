class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        nums = sorted(nums)
        original = [i for i in range(1, n+1)]
        
        diff = list(set(original) - set(nums))
        
        for j in range(1, n):
            if nums[j] == nums[j-1]:
                return [nums[j], diff[0]]
