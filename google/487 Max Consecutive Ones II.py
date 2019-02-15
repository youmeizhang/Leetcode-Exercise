class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> 'int': 
        cnt = 0
        cur = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt += 1
                cur = cnt
                cnt = 0
            res = max(res, cnt + cur)
        return res
