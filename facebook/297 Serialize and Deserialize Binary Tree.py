# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        result = []
        def preorder(root):
            if not root:
                result.append('# ')
            else:
                result.append(str(root.val) + " ")
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return ''.join(result)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        if len(data) == 0:
            return None
        vals = collections.deque(val for val in data.split())
        def build():
            if vals:
                val = vals.popleft()
                if val == '#':
                    return None
                else:
                    root = TreeNode(int(val))
                    root.left = build()
                    root.right = build()
                return root
        return build()
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
