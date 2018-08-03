#time limit
class Solution:
    def find132pattern(self, nums):
        n = len(nums)
        j = 0
        i = 0
        k = 0

        while(i < n):
            while(i < n - 1 and nums[i] >= nums[i+1]):
                i += 1
            j = i + 1
            while(j < n - 1 and nums[j] <= nums[j+1]):
                j += 1
            k = j + 1
            while(k < n):
                if nums[j] > nums[i] and nums[j] > nums[k] and nums[i] < nums[k]:
                    return True
                k += 1
            i = j + 1

        return False
