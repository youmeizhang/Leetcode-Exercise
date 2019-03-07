class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        
        def dfs(nums, tmp, i):
            self.res.append(tmp[:])
            for i in range(i, len(nums)):
                tmp.append(nums[i])
                dfs(nums, tmp, i+1)
                tmp.pop()
        dfs(nums, [], 0)
        return self.res
