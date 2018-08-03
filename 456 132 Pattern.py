class Solution:
    def find132pattern(self, nums):
        tmp = float("-inf")
        s = []
        
        for i in reversed(nums):
            if i < tmp:
                return True
            else:
                while(s and i > s[-1]):
                    tmp = s.pop()
                s.append(i)
        return False
