class Solution:
    """
    @param matrix: 
    @param x: 
    @param y: 
    @return: return the matrix
    """
    def removeOne(self, matrix, x, y):
        # Write your code here
        row = len(matrix)
        column = len(matrix[0])
        for i in range(x, row):
            if matrix[i][y] == 1:
                matrix[i][y] = 0
        return matrix
