# credit to: https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/discuss/387977/Python-Use-DFS-to-%22detect-cycle%22-(like-210.-Course-Schedule-II-and-269.-Alien-Dictionary)

class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        """
        :type n: int
        :type m: int
        :type group: List[int]
        :type beforeItems: List[List[int]]
        :rtype: List[int]
        """
        # visiting: -1
        # visited: 1
        # unvisited: 0
        def has_cycle(graph, cur_node, visited, result):
            if visited[cur_node] == 1:
                return False
            if visited[cur_node] == -1:
                return True
            visited[cur_node] = -1
            for next_node in graph[cur_node]:
                if has_cycle(graph, next_node, visited, result):
                    return True
            result.append(cur_node)
            visited[cur_node] = 1
            return False
        
        group_item_map = collections.defaultdict(list)
        visited = collections.defaultdict(dict)
        
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
            group_item_map[group[i]].append(i)
            visited[group[i]][i] = 0
        
        print(group_item_map)
        
        graph_group = collections.defaultdict(set)
        graph_item = {i: collections.defaultdict(list) for i in range(m)}
        
        for item_after, before_items in enumerate(beforeItems):
            for item_before in before_items:
                group_before = group[item_before]
                group_after = group[item_after]
                
                if group_before != group_after:
                    graph_group[group_before].add(group_after)
                else:
                    graph_item[group_before][item_before].append(item_after)
        
        visited_group = [0] * m
        group_order = []
        for group_id in range(m):
            if has_cycle(graph_group, group_id,
                              visited_group, group_order):
                return []
        
        full_item_order = []
        for group_id in group_order:
            for item_id in group_item_map[group_id]:
                if has_cycle(graph_item[group_id], item_id, visited, full_item_order):
                    return []
                
        return full_item_order[::-1]         
