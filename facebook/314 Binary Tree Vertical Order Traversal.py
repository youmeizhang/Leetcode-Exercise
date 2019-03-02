# credit to: https://blog.csdn.net/danspace1/article/details/86654851
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        if not root:
            return []
        dic = collections.defaultdict(list)
        q = [(root, 0)]
        
        while q:
            for node, col in q:
                dic[col].append(node.val)
            new_q = []
            for node, col in q:
                if node.left:
                    new_q.append((node.left, col - 1))
                if node.right:
                    new_q.append((node.right, col + 1))
            q = new_q
        
        return [dic[c] for c in sorted(dic.keys())]
    
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
