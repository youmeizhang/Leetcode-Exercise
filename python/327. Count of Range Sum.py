class FenwickTree:
    def __init__(self, n):
        self.sums = [0] * (n+1) 

    def update(self, i, delta):
        n = len(self.sums)
        while i < n:
            self.sums[i] += delta
            i += self.lowbit(i)
    
    def query(self, i):
        total = 0
        while i > 0:
            total += self.sums[i]
            i -= self.lowbit(i)
        return total
        
    def lowbit(self, i):
        return i & (-i)

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(nums)
        sums = [0] * (n+1)
        for i in range(n):
            sums[i+1] = sums[i] + nums[i]
        
        sortedSums = sorted(sums)
        ranks = {s:i+1 for i, s in enumerate(sortedSums)}
        tree = FenwickTree(n+1)
        result = 0
        for s in sums:
            result += (tree.query(bisect.bisect_right(sortedSums, s - lower)) -
                       tree.query(bisect.bisect_left(sortedSums, s-upper)))
            tree.update(ranks[s], 1)
        return result
