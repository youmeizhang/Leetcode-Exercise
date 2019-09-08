import numpy
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        l = 0
        r = 0
        prod = 1
        while r < n:
            prod *= nums[r]
            while l <= r and prod >= k:
                prod /= nums[l]
                l += 1
            ans += r - l + 1
            r += 1
        return ans
    
