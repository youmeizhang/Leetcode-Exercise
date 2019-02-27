class Solution(object):
    def maxSubArrayLen(self, nums, k):
        res = 0
        acc = 0
        dic = {0:-1}
        for i in range(len(nums)):
            acc += nums[i]
            if acc not in dic:
                dic[acc] = i
            if acc - k in dic:
                res = max(res, i - dic[acc - k])
        return res
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
