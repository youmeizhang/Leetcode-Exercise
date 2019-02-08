class Solution:
    def findLengthOfLCIS(self, nums: 'List[int]') -> 'int':
        if nums == []:
            return 0
        
        if len(list(set(nums))) == 1:
            return 1
        n = len(nums)
        res = 1
        for i in range(1, n):
            count = 1
            if nums[i] > nums[i-1]:
                count += 1
                for j in range(i+1, n):
                    if nums[j] > nums[j-1]:
                        count += 1
                    else:
                        break
            res = max(res, count)
        return res
