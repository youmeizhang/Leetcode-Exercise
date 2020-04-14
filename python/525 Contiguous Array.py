class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dic = {}
        
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
               
        prefix_sum = 0
        ans = 0
        
        for i in range(n):
            prefix_sum += nums[i]
            if prefix_sum == 0:
                ans = i + 1
            elif prefix_sum in dic:
                ans = max(ans, i - dic[prefix_sum])
            else:
                dic[prefix_sum] = i
                
        return ans
        
