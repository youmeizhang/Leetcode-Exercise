def validWordSquare(self, words):
    if len(words) == 0: return True
    if len(words) != len(words[0]): return False
    tmp = []
    matrix = []
    for i in words:
        for j in i:
            tmp.append(j)
        matrix.append(tmp)
        tmp = []
    print(matrix)
    h = len(matrix)
    w = len(matrix[0])
    for i in range(w):
        for j in range(len(matrix[i])):
            if matrix[i][j] is None and matrix[j][i] is None:
                continue
            elif matrix[i][j] == matrix[j][i]:
                continue
            else:
                return False
    return True
