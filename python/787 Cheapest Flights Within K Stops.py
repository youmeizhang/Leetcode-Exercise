# DFS

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(dict)
        for s, d, c in flights:
            graph[s][d] = c
        
        self.res = float('inf')
        self.dst =dst
        self.K = K
        
        def bfs(curr, stops, price, visited):
            if curr == self.dst:
                self.res = price
                return
            if stops > self.K:
                return

            for node, cost in graph[curr].items():
                if visited[node]:
                    continue
                if cost + price > self.res:
                    continue
                visited[node] = True

                bfs(node, stops + 1, price + cost, visited)
                visited[node] = False
          
        visited = [False] * n
        bfs(src, 0, 0, visited)
        return self.res if self.res != float('inf') else -1
        
# BFS            
 class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(dict)
        for s, d, c in flights:
            graph[s][d] = c
        
        res = float('inf')
        stop = 0
        
        q = collections.deque()
        q.append((src, 0))
        while q:
            size = len(q)
            for _ in range(size):
                curr, cost = q.popleft()
                if curr == dst:
                    res = min(res, cost)
                for v, w in graph[curr].items():
                    if w + cost > res:
                        continue
                    q.append((v, w + cost))
            stop += 1
            if stop > K + 1:
                break
        return res if res != float('inf') else -1
            
               
