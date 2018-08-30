class Solution:
    def findRelativeRanks(self, nums):
        n = len(nums)
        if n == 0: return []
        nums_new = sorted(nums, reverse = True)
        res = [0] * n
        name = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        tmp_len = 3 if n > 3 else n
        for i in range(0, tmp_len):
            res[nums.index(nums_new[i])] = name[i]
        if n > 3:
            for i in range(3, n):
                res[nums.index(nums_new[i])] = str(i + 1)
        return res
