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


class Solution(object):

    def __init__(self, nums):
        self.nums = nums
        self.dic = {}
        
        for i, num in enumerate(nums):
            if num in self.dic:
                self.dic[num].append(i)
            else:
                self.dic[num] = [i]
                
        """
        :type nums: List[int]
        """
        

    def pick(self, target):
        
        l = self.dic[target]
        return l[random.randint(0, len(l) - 1)]
                
        """
        :type target: int
        :rtype: int
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

class Solution(object):

    def __init__(self, nums):
        self.nums = nums   
        """
        :type nums: List[int]
        """
        

    def pick(self, target):
        res = None
        count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                num = random.randint(0, count)
                if num == 0:
                    res = i
                count += 1
        return res
                
        """
        :type target: int
        :rtype: int
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
