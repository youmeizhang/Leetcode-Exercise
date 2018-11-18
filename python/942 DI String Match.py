class Solution(object):
    def diStringMatch(self, S):
        n = len(S)
        dec = n
        inc = 0
        res = []
        for i in S:
            if i == "I":
                res.append(inc)
                inc += 1
            elif i == "D":
                res.append(dec)
                dec -= 1
        if S[-1] == "I":
            res.append(inc)
        else:
            res.append(dec)
        return res
