class Solution(object):
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        if row == 0:
            return False

        col = len(matrix[0]) if row else 0
        if col == 0:
            return False

        r = 0
        for i in range(1, row):
            if matrix[i-1][0] < target and matrix[i][0] > target:
                r = i-1
            elif matrix[i][0] == target or matrix[i-1][0] == target:
                return True
            elif i == row - 1 and matrix[i][0] < target:
                r = i

        if col > 1:
            for j in range(1, col):
                if matrix[r][j-1] == target or matrix[r][j] == target:
                    return True
                elif matrix[r][j-1] < target and matrix[r][j] > target:
                    return False
        else:
            if matrix[r][0] == target:
                return True
        return False        
