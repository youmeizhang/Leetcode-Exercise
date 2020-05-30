class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = collections.defaultdict(set)
        for first, later in prerequisites:
            graph[later].add(first)
        
        res = []
        
        def dfs(course, target):
            for neighbour in graph[course]:  
                if visited[neighbour]:
                    continue
                visited[neighbour] = True
                if neighbour == target or dfs(neighbour, target):
                    return True 
            return False
        
        for first, later in queries:
            visited = [False for _ in range(n)]
            if later not in graph:
                res.append(False)
                continue
            res.append(dfs(later, first))
        return res
