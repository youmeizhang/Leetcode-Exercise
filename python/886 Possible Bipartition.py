class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        color_table = [0 for i in range(N+1)]
        
        def dfs(person, color):
            color_table[person] = color
            
            for other in graph[person]:
                if color_table[other] == color:
                    return False
                
                if color_table[other] == 0 and not dfs(other, -color):
                    return False
            return True
        
        for i in range(1, N+1):
            if color_table[i] == 0 and not dfs(i, 1):
                return False
        return True
            
