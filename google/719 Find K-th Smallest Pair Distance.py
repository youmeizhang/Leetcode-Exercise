class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums = sorted(nums)
        count = [0] * (nums[-1] + 1)
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                count[nums[j] - nums[i]] += 1
        for i in range(nums[-1]):
            k -= count[i]
            if k <= 0:
                return i
        return 0
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
