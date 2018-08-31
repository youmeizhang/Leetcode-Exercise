class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack = []
        res = [-1] * n
        for x in range(n * 2):
            i = x % n
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res    
        
#Time Limit
class Solution:
    def nextGreaterElements(self, nums):
        new_nums = nums + nums
        n = len(new_nums)
        res = []
        for i in range(len(nums)):
            for j in range(i, n):
                if new_nums[j] > nums[i]:
                    res.append(new_nums[j])
                    break
                if j == n -1 and new_nums[j] <= nums[i]:
                    res.append(-1)
        return res 
