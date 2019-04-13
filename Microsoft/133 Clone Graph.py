# credit to: https://www.cnblogs.com/zuoyuan/p/3753507.html

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        def dfs(input, dic):
            if input in dic:
                return dic[input]
            output = Node(input.val, [])
            dic[input] = output
            for neighbor in input.neighbors:
                output.neighbors.append(dfs(neighbor, dic))
            return output
        
        if node is None:
            return None
        
        return dfs(node, {})
        """
        :type node: Node
        :rtype: Node
        """
        
