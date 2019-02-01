class Solution:
    def findMaxAverage(self, nums, k):
        n = len(nums)
        if k >= n:
            return sum(nums) / k
        res = float('-inf')
        for i in range(n - k + 1):
            tmp = nums[i:i+k]
            res = max(res, sum(tmp) / k)
        return res
