class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % k != 0:
            return False
        target = sum(nums) / k
        
        nums.sort()
        if nums[-1] > target:
            return False
        
        idx = n - 1
        while (idx >= 0 and nums[idx] == target):
            k -= 1
            idx -= 1
            
        def partition(subset, nums, idx, target):
            if idx < 0:
                return True
            selected = nums[idx]
            m = len(subset)
            for i in range(m):
                if (subset[i] + selected <= target):
                    subset[i] += selected
                    if partition(subset, nums, idx-1, target):
                        return True
                    subset[i] -= selected
            return False            
        
        return partition([0] * k, nums, idx, target)
    
        
        
