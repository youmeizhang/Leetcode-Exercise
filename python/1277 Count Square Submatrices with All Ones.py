class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] == 1:
                    # by checking matrix[r-1][c] and matrix[r][c-1], we know if they are 0 or 1
                    # so that we don't need to check if matrix[r][c-1] == 1 and matrix[r-1][c] == 1
                    matrix[r][c] = min(matrix[r-1][c], matrix[r][c-1], matrix[r-1][c-1]) + 1
        total = 0
        for r in range(row):
            for c in range(col):
                total += matrix[r][c]
        return total
        
