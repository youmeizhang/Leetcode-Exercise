class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        row = len(forest)
        col = len(forest[0])
        dic = {}
        
        for x in range(row):
            for y in range(col):
                if forest[x][y] > 1 or ( x == 0 and y == 0):
                    dic[forest[x][y]] = [x, y]
                    
                    
        point = sorted(dic)
        
        def bfs(x1, y1, x2, y2, visited):
            row = len(forest)
            col = len(forest[0])
            queue = []
            queue.append([[x1, y1]])

            while queue:
                path = queue.pop(0)
                node = path[-1]
                
                x = node[0]
                y = node[1]
                visited[x][y] = True
                if node == [x2, y2]:
                    return len(path) - 1

                for dx, dy in zip([0,1,0,-1], [1,0,-1,0]):
                    new_x = x + dx
                    new_y = y + dy
                      
                    if new_x in range(row) and new_y in range(col) and not visited[new_x][new_y] and forest[new_x][new_y] > 0:
                        new_path = list(path)
                        new_path.append([new_x, new_y])
                    
                        if new_path not in queue:
                            queue.append(new_path)
            return -1
        
        n = len(point)
        self.res = 0
        if point[0] != [0, 0]:
            self.res += bfs(0, 0, dic[point[0]][0], dic[point[0]][1], [[False] * col for _ in range(row)])
            
        for i in range(n-1):
            visited = [[False] * col for _ in range(row)]
            x1, y1 = dic[point[i]][0], dic[point[i]][1]
            x2, y2 = dic[point[i+1]][0], dic[point[i+1]][1]
            
            ans = bfs(x1, y1, x2, y2, visited)
            if ans == -1:
                return -1
            else:
                self.res += ans

                forest[x1][y1] = 1
        
        return self.res
