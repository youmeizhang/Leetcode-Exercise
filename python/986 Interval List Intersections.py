# Important point: if lowest endpoint is in A then we know there is only interval in B can intersect with A. Because pair in B is disjoint. In this assumption, we can discard A after intersecting

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        m = len(A)
        n = len(B)
        res = []
        while i < m and j < n:
            min_value = max(A[i][0], B[j][0])
            
            if A[i][1] <= B[j][1]:
                if min_value <= A[i][1]:
                    res.append([min_value, A[i][1]])
                i += 1
            else:
                if min_value <= B[j][1]:
                    res.append([min_value, B[j][1]])
                j += 1
        return res
            
