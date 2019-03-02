class Solution(object):
    def search(self, nums, target):
        if nums == []:
            return False
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        n = len(nums)
        if nums[0] > target:
            for i in range(min_idx, n):
                if nums[i] == target:
                    return True
                else:
                    continue
        else:
            for i in range(0, max_idx+1):
                if nums[i] == target:
                    return True
                else:
                    continue
        return False
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
