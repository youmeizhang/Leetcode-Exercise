# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dimension = binaryMatrix.dimensions()
        row, col = dimension[0], dimension[1]
        res = []
        
        for i in range(row):
            left = 0
            right = col - 1
            leftmost = float('inf')
            while left <= right:
                mid = (left + right) // 2
                if binaryMatrix.get(i, mid) == 1:
                    leftmost = min(leftmost, mid)
                    right = mid - 1
                else:
                    left = mid + 1
            res.append(leftmost)
        
        idx = min(res)
        if idx == float('inf'):
            return -1
        else:
            return idx
