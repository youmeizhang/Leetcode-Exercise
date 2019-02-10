class Solution:
    def gameOfLife(self, board: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        column = len(board[0])
        for i in range(row):
            for j in range(column):
                count = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if i + dx >= 0 and i + dx < row and j + dy >= 0 and j + dy < column:
                            if board[i+dx][j+dy] == 1 or board[i+dx][j+dy] == 2:
                                if dx == 0 and dy == 0:
                                    continue
                                else:
                                    count += 1
                            else:
                                continue
                        else:
                            continue
                if count > 3 or count < 2:
                    if board[i][j] == 1:
                        board[i][j] = 2

                elif count == 3:
                    if board[i][j] == 0:
                        board[i][j] = 3
                        
        for p in range(row):
            for q in range(column):
                board[p][q] = board[p][q] % 2
