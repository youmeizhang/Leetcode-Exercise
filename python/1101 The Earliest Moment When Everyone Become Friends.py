class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        logs = sorted(logs, key=lambda x:x[0])
        parent = {}
        res = []
        n = len(logs)
        
        for i in range(N):
            parent[i] = i
        
        for i in range(n):
            #print(i)
            self.union(parent, logs[i][1], logs[i][2])
            l = list(parent.values())
            pare = self.find(parent, l[0])
            count = 1
            for j in range(1, len(l)):
                if self.find(parent, l[j]) == pare:
                    count += 1
            if count == len(l):
                return logs[i][0]

        return -1
        
    def find(self, parent, a):
        if parent[a] != a:
            parent[a] = self.find(parent, parent[a])
        return parent[a]

    def union(self, parent, a, b):
        pa = self.find(parent, a)
        pb = self.find(parent, b)
        if pa != pb:
            parent[pa] = pb
