class Solution(object):
    def permuteUnique(self, nums):
        nums = sorted(nums)
        
        self.res = []
        self.visit = [False] * len(nums)
        
        def dfs(nums, tmp):
            if len(nums) == len(tmp):
                self.res.append(tmp[:])
                
            for i in range(len(nums)):
                if self.visit[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and self.visit[i-1]:
                    continue
                tmp.append(nums[i])
                self.visit[i] = True
                dfs(nums, tmp)
                self.visit[i] = False
                tmp.pop()
        dfs(nums, [])
        return self.res
            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
