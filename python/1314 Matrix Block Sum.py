# credit to: https://leetcode.com/problems/matrix-block-sum/discuss/477036/JavaPython-3-PrefixRange-sum-w-analysis-similar-to-LC-30478
class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        row = len(mat)
        col = len(mat[0])
        rangeSum = [[0] * (col+1) for _ in range(row+1)]
        
        for r in range(row):
            for c in range(col):
                rangeSum[r+1][c+1] = rangeSum[r][c+1] + rangeSum[r+1][c] + mat[r][c] - rangeSum[r][c]
        
        res = [[0] * col for _ in range(row)]
        for r in range(row):
            for c in range(col):
                c1 = max(c - K, 0)
                r1 = max(r - K, 0)
                c2 = min(c + K + 1, col)
                r2 = min(r + K + 1, row)
                res[r][c] = rangeSum[r2][c2] - rangeSum[r2][c1] - rangeSum[r1][c2] + rangeSum[r1][c1]
        return res
