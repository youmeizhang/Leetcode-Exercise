#TIME LIMIT
class Solution:
    def makesquare(self, nums):
        n = len(nums)
        total = sum(nums)
        
        if total % 4 != 0 or total == 0:
            return False
        
        nums = sorted(nums, reverse = True)
        length = [total // 4 for i in range(0, 4)]
        
        return self.dfs(nums, length, 0)
    
    def dfs(self, nums, length, pos):
        if pos == len(nums):
            return True
        for idx in range(4):
            if length[idx] >= nums[pos]:
                length[idx] -= nums[pos]
                if self.dfs(nums, length, pos + 1):
                    return True
                length[idx] += nums[pos]
        return False
