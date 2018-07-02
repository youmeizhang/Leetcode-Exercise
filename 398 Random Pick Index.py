class Solution(object):

    def __init__(self, nums):
        self.nums = nums
        """
        :type nums: List[int]
        """
        

    def pick(self, target):
        dic = {}
        for i in range(len(self.nums)):
            if self.nums[i] in dic:
                dic[self.nums[i]].append(i)
            else:
                dic[self.nums[i]] = [i]
                
        return random.choice(dic[target])
