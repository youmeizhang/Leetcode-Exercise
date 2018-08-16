class Solution(object):
    def transpose(self, A):
        w = len(A[0])
        h = len(A)
        tmp = []
        res = []
        for i in range(w):
            for j in range(h):
                tmp.append(A[j][i])
            res.append(tmp)
            tmp = []
        return res
