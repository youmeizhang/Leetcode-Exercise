class Solution(object):
    def numRookCaptures(self, board):
        row = len(board)
        column = len(board[0])
        for i in range(row):
            for j in range(column):
                if board[i][j] == "R":
                    x = i
                    y = j
                    break
        i = x
        j = y
        count = 0

        while x >= 0:
            if board[x][y] == "p":
                count += 1
                break
            elif board[x][y] == "B":
                break
            else:
                x -= 1

        x = i
        y = j
        
        while x < row:
            if board[x][y] == "p":
                count += 1
                break
            elif board[x][y] == "B":
                break
            else:
                x += 1

        x = i
        y = j

        while y >= 0:
            if board[x][y] == "p":
                count += 1
                break
            elif board[x][y] == "B":
                break
            else:
                y -= 1

        x = i
        y = j       

        while y < column:
            if board[x][y] == "p":
                count += 1
                break
            elif board[x][y] == "B":
                break
            else:
                y += 1
        return count
        """
        :type board: List[List[str]]
        :rtype: int
        """

