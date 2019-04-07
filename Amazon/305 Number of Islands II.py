# credit to: https://leetcode.com/problems/number-of-islands-ii/discuss/245650/Python-UnionFind-simple-solution

class Solution(object):
    def numIslands2(self, m, n, positions):
        parent = [-1] * (m * n)
        res = []
        count = 0
        rank = [0] * (m * n)
        
        dxs = [-1, 0, 1, 0]
        dys = [0, 1, 0, -1]
        
        for pos in positions:
            x, y = pos[0], pos[1]
            idn = n*x + y
            if parent[idn] == -1:
                parent[idn] = idn
                count += 1
            
            for dx, dy in zip(dxs, dys):
                nx = dx + x
                ny = dy + y
                newIdn = nx*n+ny
                if nx < 0 or nx >= m or ny < 0 or ny >= n or parent[newIdn] == -1:
                    continue
                
                p = self.find(parent, newIdn)
                q = self.find(parent, idn)
                if p != q:

                    self.union(rank, parent, p, q)
                    count -= 1

            res.append(count)
        return res
    
    def find(self, parent, idn):
        if parent[idn] != idn:
            idn = self.find(parent, parent[idn])
        return idn

    def union(self, rank, parent, p, q):
        if rank[p] > rank[q]:
            parent[q] = p
        elif rank[p] < rank[q]:
            parent[p] = q
        else:
            parent[q] = p
            rank[p] += 1
        
