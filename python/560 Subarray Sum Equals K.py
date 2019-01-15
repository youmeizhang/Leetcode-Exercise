class Solution(object):
    def subarraySum(self, nums, k):
        dic = collections.defaultdict(int)
        dic[0] = 1
        res = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total - k in dic:
                res += dic[total - k]
            dic[total] += 1
        return res
