# credit to: https://leetcode.com/problems/count-submatrices-with-all-ones/discuss/725108/Python-3-Dynamic-Programming

class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        row = len(mat)
        col = len(mat[0])

        for r in range(row):
            for c in range(1, col):
                if mat[r][c]:
                    mat[r][c] = mat[r][c-1] + 1
        
        print(mat)
        
        res = 0
        for r in range(row):
            for c in range(col):
                if mat[r][c]:
                    ro = r
                    min_ = mat[r][c]
                    while ro < row and mat[ro][c]:
                        min_ = min(min_, mat[ro][c])
                        res += min_
                        ro += 1
        return res
    
