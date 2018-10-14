class Solution:
    def minAddToMakeValid(self, S):
        if len(S) == 0:
            return 0
        count = 0
        res = 0
        
        for i in S:
            if i == "(":
                count += 1
            else:
                count -= 1
                
            if count < 0:
                res += 1
                count = 0
        return res + count
