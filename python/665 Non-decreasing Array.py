class Solution:
    def checkPossibility(self, nums: 'List[int]') -> 'bool':
        a = nums[:]
        b = nums[:]
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                a[i - 1] = nums[i]
                b[i] = nums[i - 1]
                break
                
        return a == sorted(a) or b == sorted(b)
