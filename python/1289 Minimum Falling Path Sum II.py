from heapq import nsmallest

class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        row = len(arr)
        col = len(arr[0])
        
        for r in range(1, row):
            fm, sm = nsmallest(2, arr[r-1])

            for c in range(col):
                if fm == arr[r-1][c]:
                    arr[r][c] += sm

                else:
                    arr[r][c] += fm

        return min(arr[-1])
