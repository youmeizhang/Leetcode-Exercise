class Solution(object):

    def __init__(self, nums):
        self.nums = nums
        """
        :type nums: List[int]
        """
        

    def pick(self, target):
        idx = []
        for i, num in enumerate(self.nums):
            if num == target:
                idx.append(i)
        return idx[random.randint(0, len(idx) - 1)]
                
        """
        :type target: int
        :rtype: int
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
