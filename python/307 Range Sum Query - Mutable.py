class SegmentedTreeNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None



class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums) - 1
        
        def buildNode(start, end, nums):
            if start > end:
                return None
            
            if start == end:
                root = SegmentedTreeNode(start, end)
                root.sum = nums[start]
                return root
            
            mid = (start + end) // 2
            root = SegmentedTreeNode(start, end)
            root.left = buildNode(start, mid, nums)
            root.right = buildNode(mid+1, end, nums)
            
            root.sum = root.left.sum + root.right.sum
            return root
        
        self.root = buildNode(0, n, nums)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        def updateTree(root, idx, val):
            if root.start == root.end:
                root.sum = val
                return val
            mid = (root.start + root.end) // 2
            if i > mid:
                updateTree(root.right, idx, val)
            else:
                updateTree(root.left, idx, val)
            root.sum = root.left.sum + root.right.sum
            return root.sum
        
        return updateTree(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def querySum(root, i, j):
            if root.start == i and root.end == j:
                return root.sum
            mid = (root.start + root.end) // 2
            if j <= mid:
                return querySum(root.left, i, j)
            elif i > mid:
                return querySum(root.right, i, j)
            else:
                return querySum(root.left, i, mid) + querySum(root.right, mid + 1, j)
    
        return querySum(self.root, i, j)
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
