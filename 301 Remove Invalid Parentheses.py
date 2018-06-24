class Solution(object):
    def removeInvalidParentheses(self, s):
        if not s: return ['']
        q = {s}
        while q:
            ans = filter(self.isValidParentheses, q)
            if ans:
                return ans
            q = {cur[:i] + cur[i+1:] for cur in q for i in range(len(cur))}

    def isValidParentheses(self, s):
        count = 0
        for i in s:
            if i == "(":
                count += 1
            elif i == ")":
                if count == 0:
                    return False
                count -= 1
        return count == 0
