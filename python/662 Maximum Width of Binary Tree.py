class Solution:
    def widthOfBinaryTree(self, root):
        queue = collections.deque()
        queue.append((root, 1))
        res = float('-inf')
        while(queue):
            width = queue[-1][1] - queue[0][1] + 1
            res = max(res, width)
            
            for _ in range(len(queue)):
                node, count = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*count))
                if node.right:
                    queue.append((node.right, 2*count + 1))
        return res
                
