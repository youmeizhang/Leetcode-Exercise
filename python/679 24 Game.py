# credit to: https://www.youtube.com/watch?v=3zXaIOX1ezU

class Solution(object):
    def judgePoint24(self, nums):
        new_nums = []
        for x in nums:
            new_nums.append(x * 1.0)
            
        return self.helper(new_nums)
    
    def helper(self, nums):
        n = len(nums)
        if n == 1:
            return abs(nums[0] - 24) < 1e-6
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                else:
                    a = nums[i]
                    b = nums[j]
                    tmp = a + b
                    newNums = []
                    for x in range(n):
                        if x != i and x != j:
                            newNums.append(nums[x])
                            
                    newNums.append(tmp)
                    if self.helper(newNums):
                        return True
                    
                    tmp = a - b
                    newNums[-1] = tmp
                    if self.helper(newNums):
                        return True
                    
                    tmp = a * b
                    newNums[-1] = tmp
                    if self.helper(newNums):
                        return True
                    
                    if b != 0:
                        tmp = a / b
                        newNums[-1] = tmp
                        if self.helper(newNums):
                            return True
        return False
    
#credit to: http://bookshadow.com/weblog/2017/09/17/leetcode-24-game/

class Solution(object):
    def judgePoint24(self, nums):
        return any(abs(x-24) < 1e-9 for x in self.solver(nums))
    
    def solver(self, nums):
        size = len(nums)
        if size == 1:
            return [nums[0]]
        ans = []
        for x in range(size):
            left, n = nums[x], nums[:x] + nums[x+1:]
            for right in self.solver(n):
                ans.append(left + right)
                ans.append(left - right)
                ans.append(left * right)
                if right:
                    ans.append(1.0 * left / right)
        if size >= 3:
            for x in range(size):
                for y in range(x+1, size):
                    left, right = nums[x], nums[y]
                    n = nums[:x] + nums[x+1:y] + nums[y+1:]
                    ans += self.solver([left+right] + n)
                    ans += self.solver([left-right] + n)
                    ans += self.solver([left*right] + n)
                    if right:
                        ans += self.solver([1.0*left/right])
        return ans

        """
        :type nums: List[int]
        :rtype: bool
        """
        
