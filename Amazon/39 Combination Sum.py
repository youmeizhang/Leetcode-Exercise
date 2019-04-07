# credit to: https://www.youtube.com/watch?v=HdS5dOaz-mk

class Solution(object):
    def combinationSum(self, nums, target):
        self.res = []
        def dfs(nums, temp, target, index):
            if target == 0:
                self.res.append(temp[:])
                return
            if target < 0:
                return
            
            for i in range(index, len(nums)):
                temp.append(nums[i])
                dfs(nums, temp, target - nums[i], i)
                temp.pop()
                
        dfs(nums, [], target, 0)
        return self.res
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
