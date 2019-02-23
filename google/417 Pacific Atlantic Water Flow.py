class Solution(object):
    def pacificAtlantic(self, matrix):
        if matrix == []:
            return []
        
        row = len(matrix)
        column = len(matrix[0])

        def checkPacific(i, j, matrix, visited, row, column):
            visited[i][j] = True
            for dx, dy in zip([-1, 0, 1, 0], [0, -1, 0, 1]):

                x = i + dx
                y = j + dy

                if x < 0 or y < 0:
                    return True

                if x >= 0 and y >= 0 and x < row and y < column and not visited[x][y]:
                    if matrix[x][y] <= matrix[i][j]:
                        if checkPacific(x, y, matrix, visited, row, column):
                            return True

            return False

        def checkAtlantic(i, j, matrix, visited, row, column):
            visited[i][j] = True
            for dx, dy in zip([0,1,0,-1], [1,0,-1,0]):
                x = i + dx
                y = j + dy

                if x >= row or y >= column:
                    return True   

                if x >= 0 and y >= 0 and x < row and y < column and not visited[x][y]:
                    if matrix[x][y] <= matrix[i][j]:
                        if checkAtlantic(x, y, matrix, visited, row, column):
                            return True

            return False

        res = []
        for i in range(row):
            for j in range(column):
                visited = [[False] * column for _ in range(row)]
                #just be careful of the "visited", need to define new one
                if checkPacific(i, j, matrix, visited, row, column) and checkAtlantic(i, j, matrix, [[False] * column for _ in range(row)], row, column):
                    res.append([i, j])

        return res
