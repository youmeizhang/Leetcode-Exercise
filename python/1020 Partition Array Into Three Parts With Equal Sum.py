class Solution(object):
    def canThreePartsEqualSum(self, A):
        n = len(A)
        if n < 3:
            return False
        s = sum(A) / 3
        count = 0
        total = 0
        for i in range(n):
            if total == s:
                total = A[i]
                count += 1
            else:
                total += A[i]
        if total == s:
            count += 1
        return count == 3
            
        
                
        """
        :type A: List[int]
        :rtype: bool
        """
        
