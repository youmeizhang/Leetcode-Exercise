class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visit = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        self.res = []
        
        for x, y in prerequisites:
            graph[x].append(y)
            
        #visiting: 1
        #unvisit: 0
        #visited: -1
        
        #dfs return:
        #false: has cycle
        #true: no cycle
        
        def dfs(node):
            if visit[node] == -1:
                return True
            if visit[node] == 1:
                return False
            visit[node] = 1
            
            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            visit[node] = -1
            self.res.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return self.res
