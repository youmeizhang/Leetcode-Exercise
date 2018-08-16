class Solution(object):
    def maxRotateFunction(self, A):
        sumA = 0
        n = len(A)
        if n == 0:
            return 0
        w = list(range(0, len(A)))
        for i in range(len(w)):
            sumA += w[i] * A[i]
        total = [sumA]
        totalsum = sum(A)
        for i in range(len(A)):
            tmp = totalsum - n * A[n - i - 1]
            total.append(total[i] + tmp)
        return max(total)
