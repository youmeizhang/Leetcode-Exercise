class Solution(object):
    def multiply(self, A, B):
        row_A = len(A)
        row_B = len(B)
        col_A = len(A[0])
        col_B = len(B[0])
        res = [[0] * col_B for _ in range(row_A)]

        for i in range(row_A):
            for q in range(col_B):
                tmp = 0

                for j in range(col_A):
                    tmp += A[i][j] * B[j][q]
                res[i][q] = tmp 

        return res   
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
