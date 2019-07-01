# credit to: https://www.youtube.com/watch?v=0Y0NybskQFc

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        row = len(A)
        col = len(A[0])
        
        q = [[-A[0][0], 0, 0]]
        res = float('inf')
        visited = set((0, 0))
        
        while True:
            sc, x, y = heapq.heappop(q)
            res = min(res, -sc)
            if x == row - 1 and y == col - 1:
                return res
            for dx, dy in zip([0,1,0,-1],[1,0,-1,0]):
                new_x = dx + x
                new_y = dy + y
                if new_x in range(0, row) and new_y in range(0, col) and (new_x, new_y) not in visited:
                    heapq.heappush(q, [-A[new_x][new_y], new_x, new_y])
                    visited.add((new_x, new_y))
            
        
        
