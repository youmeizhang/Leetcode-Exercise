class Solution:
    def totalHammingDistance(self, nums):
        ans = 0
        for i in range(32):
            mask = 1 << i
            zero = one = 0
            for num in nums:
                if num & mask:
                    one += 1
                else:
                    zero += 1
            ans += zero * one
        return ans

#Time limit
class Solution:
    def totalHammingDistance(self, nums):
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                ans += bin(nums[i] ^ nums[j]).count('1')
        return ans
