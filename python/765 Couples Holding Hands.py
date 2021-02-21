class UnionFind:
    def __init__(self, n):
        self.parents = [0] * n
        self.ranks = [0] * n
        self.count = n
        for i in range(n):
            self.parents[i] = i
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        elif px < py:
            self.parents[px] = py
            self.ranks[py] += 1
        else:
            self.parents[py] = px
            self.ranks[px] += 1
        self.count -= 1
        
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        uf = UnionFind(n)
        for i in range(n):
            x = i * 2
            y = i * 2 + 1
            uf.union(row[x] // 2, row[y] // 2)
        return n - uf.count
        
        
