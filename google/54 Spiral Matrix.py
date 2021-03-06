class Solution:
    def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if matrix == []: 
            return []
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        res = []
        direction = 0
        while True:
            if direction == 0:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up += 1
            if direction == 1:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1
            if direction == 2:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
            if direction == 3:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            if left > right or up > down:
                return res
            direction = (direction + 1) % 4
