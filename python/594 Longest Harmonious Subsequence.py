class Solution(object):
    def findLHS(self, nums):
        dic = collections.Counter(nums)
        num = sorted(list(set(nums)))
        res = 0

        for i in range(1, len(num)):
            if num[i] - num[i-1] == 1:
                res = max(res, dic[num[i]] + dic[num[i-1]])
        return res
