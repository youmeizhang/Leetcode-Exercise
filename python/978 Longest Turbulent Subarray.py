class Solution(object):
    def maxTurbulenceSize(self, A):
        n = len(A)
        first = [1] * n
        second = [1] * n
        B = list(reversed(A))

        for i in range(1, n):
            if i % 2 == 1:
                if B[i] > B[i-1]:
                    #print("i is: ", i)
                    first[i] = first[i-1] + 1
                else:
                    continue

            if i % 2 == 0:
                if B[i] < B[i-1]:
                    #print("i is: ", i)
                    first[i] = first[i-1] + 1
                else:
                    continue

        for i in range(1, n):
            if i % 2 == 0:
                if A[i] < A[i-1]:
                    second[i] = second[i-1] + 1  
                else:
                    continue
            if i % 2 == 1:
                if A[i] > A[i-1]:
                    second[i] = second[i-1] + 1
                else:
                    continue

        return max(max(first), max(second))
