class Solution(object):
    def largestPerimeter(self, A):
        A = sorted(A, reverse = True)

        for i in range(1, len(A)):
            for j in range(i+1, len(A)):
                if A[i - 1] < A[i] + A[j]:
                    return A[i - 1] + A[i] + A[j]
                elif A[i - 1] > A[i] + A[j]:
                    j += 1
                else:
                    i += 1
                    j += 1
        return 0
