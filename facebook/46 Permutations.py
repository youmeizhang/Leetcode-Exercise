class Solution(object):
    def permute(self, nums):
        
        self.res = []
        
        def dfs(nums, tmp):
            if len(nums) == len(tmp):
                self.res.append(tmp[:])
            
            for i in range(len(nums)):
                if nums[i] in tmp:
                    continue
                tmp.append(nums[i])
                dfs(nums, tmp)
                tmp.pop()
        dfs(nums, [])
        return self.res
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
