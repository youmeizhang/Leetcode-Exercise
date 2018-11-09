def roverMove(matrixSize, cmds):
    # Write your code here
    def check(x, y, matrixSize):
        if x < matrixSize and y < matrixSize and x >= 0 and y >= 0:
            return True
        return False
    x = 0 
    y = 0
    cmds = list(reversed(cmds))
    while (cmds):
        tmp = cmds.pop()
        if tmp == "LEFT":
            if check(x, y-1, matrixSize):
                y -= 1
            else:
                continue
        elif tmp == "RIGHT":
            if check(x, y+1, matrixSize):
                y += 1
            else:
                continue
        elif tmp == "UP":
            if check(x-1, y, matrixSize):
                x -= 1
            else:
                continue
        elif tmp == "DOWN":
            if check(x+1, y, matrixSize):
                x += 1
            else:
                continue
    return x * matrixSize + y
