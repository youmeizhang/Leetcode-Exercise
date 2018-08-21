#1
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        nums_new = ''.join(str(x) for x in nums)
        tmp = nums_new.split('0')
        res = 0
        for i in tmp:
            res = max(res, len(i))
        return res

#2
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        res = 0
        for i in nums:
            if i == 0:
                res = max(res, count)
                count = 0
            else:
                count += 1
        return max(res, count)
