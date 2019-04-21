class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        res = [[r0, c0]]
        queue = [[r0, c0]]
        visited = [[False] * C for _ in range(R)]
        visited[r0][c0] = True
        while queue:
            pos = queue.pop(0)
            for dx, dy in zip([0,1,0,-1], [1,0,-1,0]):
                x = pos[0] + dx
                y = pos[1] + dy
                if x in range(R) and y in range(C) and not visited[x][y]:
                    queue.append([x, y])
                    res.append([x, y])
                    visited[x][y] = True
        return res
        
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        
