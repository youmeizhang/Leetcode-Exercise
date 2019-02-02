class Solution:
    def imageSmoother(self, M):
        row = len(M)
        column = len(M[0])
        res = [[0] * column for _ in range(row)]
        
        for i in range(row):
            for j in range(column):
                tmp = []
                for p in range(i-1, i+2):
                    for q in range(j-1, j+2):
                        if p >= 0 and p < row and q >= 0 and q < column:
                            tmp.append(M[p][q])

                res[i][j] = math.floor(sum(tmp) /  len(tmp))
                
        return res
