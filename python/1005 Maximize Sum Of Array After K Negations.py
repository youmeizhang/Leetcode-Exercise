#credit to: https://www.geeksforgeeks.org/maximize-array-sun-after-k-negation-operations/

class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        n = len(A)
        for i in range(1, K + 1): 
            min = +2147483647
            index = -1
            for j in range(n): 

                if (A[j] < min): 

                    min = A[j] 
                    index = j 

            if (min == 0): 
                break

            A[index] = -A[index] 
        sum = 0
        for i in range(n): 
            sum += A[i] 
        return sum
