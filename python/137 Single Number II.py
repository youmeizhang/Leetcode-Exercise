# bitwise solution reference: https://www.youtube.com/watch?v=ny1tk1AkON8
# important notes:

# 1. How to check if any number has set bit on ith position?
# (num & (1<<i)) != 0

# 2. How to set bit on ith position in any number?
# num = num | (1 << i)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       
        res = 0
        n = len(nums)
        for i in range(32):
            cnt = 0
            for j in range(n):
                if nums[j] & (1<<i) != 0:
                    cnt += 1
            
            res = res | ((cnt % 3) << i )
        return res - 2**32 if res >= 2**31 else res
    
