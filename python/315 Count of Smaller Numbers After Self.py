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

# use Fenwick Tree to update the frequency list because each time when looping through the array, we will update the frequency.

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        set_nums = set(nums)
        dic = {}
        rank = 1
        sorted_set = sorted(set_nums)
        for num in sorted_set:
            dic[num] = rank
            rank += 1
        
        res = []
        tree = FenwickTree(n+1)
        for i in range(n-1, -1, -1):
            rank = dic[nums[i]]
            total = tree.query(rank-1)
            res.append(total)
            tree.update(rank, 1)
            
        return res[::-1]
        
