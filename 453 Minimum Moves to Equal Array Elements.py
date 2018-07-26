class Solution:
    def minMoves(self, nums):
        n = len(nums)
        return sum(nums) - min(nums) * n
