class Solution(object):
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        i = 0
        j = -1
        
        max_val = float('-inf')
        min_val = float('inf')
        
        r = n - 1
        
        for l in range(n):
            max_val = max(max_val, nums[l])
            if (max_val != nums[l]):
                j = l
            min_val = min(min_val, nums[r])
            if (min_val != nums[r]):
                i = r
            r -= 1
        
        return j - i + 1
