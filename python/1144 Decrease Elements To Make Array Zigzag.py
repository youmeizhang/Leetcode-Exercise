# credit to: https://www.youtube.com/watch?v=R0Re58WF6Do

class Solution:
    def movesToMakeZigzag(self, nums):
        nums = [float('inf')] + nums + [float('inf')]
        n = len(nums)
        res = [0, 0]
        for i in range(1, n-1):
            res[i % 2] += max(0, nums[i] - min(nums[i-1], nums[i+1]) + 1)
        return min(res)
        
