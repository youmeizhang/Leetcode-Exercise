class Solution(object):
    def removeOuterParentheses(self, S):
        count = 0
        n = len(S)
        start = 0
        end = 0
        res = []
        for i in range(n):
            if S[i] == "(":
                count += 1
            else:
                count -= 1

            if count == 0:
                end = i+1
                res.append(S[start+1:end-1])
                start = i+1
        return ''.join(res)
        """
        :type S: str
        :rtype: str
        """
        
