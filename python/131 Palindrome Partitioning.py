class Solution(object):
    def isPalindrome(self, a):
        result = [i for i in a.lower() if i.isalnum()]
        if result == result[::-1]:
            return True
        else:
            return False

    def dfs(self, s, resultlist):
        if len(s) == 0: Solution.res.append(resultlist)
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], resultlist + [s[:i]])

    def partition(self, s):
        Solution.res = []
        self.dfs(s, [])
        return Solution.res
