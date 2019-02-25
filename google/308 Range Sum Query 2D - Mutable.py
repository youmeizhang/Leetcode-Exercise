class NumMatrix(object):

    def __init__(self, matrix):
        self.matrix = matrix
        """
        :type matrix: List[List[int]]
        """
        

    def update(self, row, col, val):
        self.matrix[row][col] = val
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        

    def sumRegion(self, row1, col1, row2, col2):
        total = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                total += self.matrix[i][j]
        return total
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
