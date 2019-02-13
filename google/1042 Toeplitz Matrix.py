class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        # Write your code here
        row = len(matrix)
        column = len(matrix[0])
        
        for diff in range(-row, column):
            count = 0
            for i in range(row):
                j = diff + i
                if j >= 0 and j < column:
                    if count == 0:
                        ele = matrix[i][j]
                    else:
                        if matrix[i][j] != ele:
                            return False
                    count += 1
                else:
                    continue
        return True
