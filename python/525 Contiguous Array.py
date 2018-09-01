class Solution:
    def findMaxLength(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        dic = {}
        tmp_sum = 0
        ans = 0
        for i in range(len(nums)):
            tmp_sum += nums[i]
            if tmp_sum == 0:
                ans = i + 1
            elif tmp_sum not in dic:
                dic[tmp_sum] = i
            else:
                ans = max(ans, i - dic[tmp_sum])
        return ans
