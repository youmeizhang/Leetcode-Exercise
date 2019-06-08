# credit to: https://blog.csdn.net/zjucor/article/details/90738550

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        res = []
        n = len(matrix[0])
        for row in matrix:
            a = [str(i) for i in range(n) if row[i] == 1]
            b = [str(i) for i in range(n) if row[i] == 0]
            res.append(''.join(a))
            res.append(''.join(b))
        dic = collections.Counter(res)
        return max(dic.values())
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
