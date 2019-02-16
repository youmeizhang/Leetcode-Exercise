class Solution:
    def calcEquation(self, equations: 'List[List[str]]', values: 'List[float]', queries: 'List[List[str]]') -> 'List[float]':
        def dfs(x, y, table, visited):
            if x == y:
                return 1.0
            visited.add(x)
            for n in table[x]:
                if n in visited:
                    continue
                res = dfs(n, y, table, visited)
                if res > 0:
                    return res * table[x][n]
            return -1.0

        table = collections.defaultdict(dict)
        for (x, y), value in zip(equations, values):
            table[x][y] = value
            table[y][x] = 1 / value
        ans = []
        for (x, y) in queries:
            if x in table and y in table:
                ans.append(dfs(x, y, table, set()))
            else:
                ans.append(-1.0)
        return ans
