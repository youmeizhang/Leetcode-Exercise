# credit to: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space

class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i-1:i] + arr[i+1:i+2]) * arr.pop(i)
        return res
        
