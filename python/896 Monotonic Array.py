class Solution:
    def isMonotonic(self, A):
        n = len(A)
        if n < 2:
            return True
        
        def isDecreasing(A):
            n = len(A)
            for i in range(1, n):
                if A[i] <= A[i - 1]:
                    continue
                else:
                    return False
            return True
        
        for i in range(1, n):
            if A[i] >= A[i - 1]:
                    continue
            elif isDecreasing(A):
                return True
            else:
                return False
        return True
            
