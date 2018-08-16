class Solution(object):
    def calcEquation(self, equations, values, queries):
        matrix = collections.defaultdict(lambda: collections.defaultdict(int))
        for (s, t), v in zip(equations, values):
            matrix[s][t] = v
            matrix[t][s] = 1.0 / v

        for k in matrix:
            matrix[k][k] = 1.0
            for s in matrix:
                for t in matrix:
                    if matrix[s][k] and matrix[k][t]:
                        matrix[s][t] = matrix[s][k] * matrix[k][t]
        ans = []
        for s, t in queries:
            if matrix[s][t]:
                ans.append(matrix[s][t])
            else:
                ans.append(-1)
        return ans
