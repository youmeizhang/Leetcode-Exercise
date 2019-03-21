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
        
