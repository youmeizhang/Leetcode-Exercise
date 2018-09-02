class Solution:
    def checkSubarraySum(self, nums, k):
        dic = {0: -1}
        summ = 0
        for i, n in enumerate(nums):
            summ += n
            m = summ % k if k else summ
            if m not in dic: dic[m] = i
            elif dic[m] + 1 < i: return True
        return False
        
#Time Limit
class Solution:
    def checkSubarraySum(self, nums, k):
        n = len(nums)
        for i in range(2, n + 1):
            tmp = 0
            for j in range(0, n-i+1):
                tmp += sum(nums[j:j+i])
                if k != 0:
                    if tmp % k == 0:
                        return True
                elif k == 0 and tmp == 0:
                    return True
                tmp = 0
        return False
