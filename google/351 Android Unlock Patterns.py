#credit to: http://www.cnblogs.com/grandyang/p/5541012.html

class Solution(object):
    def numberOfPatterns(self, m, n):
        matrix = [[0] * 10 for _ in range(10)]
        matrix[1][3] = matrix[3][1] = 2
        matrix[1][7] = matrix[7][1] = 4
        matrix[3][9] = matrix[9][3] = 6
        matrix[7][9] = matrix[9][7] = 8
        matrix[1][9] = matrix[9][1] = matrix[4][6] = matrix[6][4] = matrix[2][8] = matrix[8][2] = matrix[3][7] = matrix[7][3] = 5
        visited = [False] * 10

        def helper(num, length, res, m, n, matrix, visited):
            if length >= m:
                res += 1
            length += 1
            if length > n:
                return res
            visited[num] = True
            for i in range(1, 10):
                jump = matrix[num][i]
                if not visited[i] and (jump == 0 or visited[jump]):
                    res = helper(i, length, res, m, n, matrix, visited)
            visited[num] = False
            return res

        res = 0

        res += helper(1, 1, 0, m, n, matrix, visited) * 4
        res += helper(2, 1, 0, m, n, matrix, visited) * 4
        res += helper(5, 1, 0, m, n, matrix, visited)
        return res  
        """
        :type m: int
        :type n: int
        :rtype: int
        """
