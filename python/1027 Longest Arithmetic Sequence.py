class Solution(object):
    def longestArithSeqLength(self, A):
        n = len(A)
        dic = collections.defaultdict()

        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                if (A[i] - A[j]) in dic:
                    dic[A[i] - A[j]][i] = max(dic[A[i] - A[j]][i], dic[A[i] - A[j]][j] + 1)
                else:
                    dic[A[i] - A[j]] = [1] * n
                    dic[A[i] - A[j]][i] += 1

        res = 1

        for key in dic:
            res = max(res, max(dic[key]))
        return res
        """
        :type A: List[int]
        :rtype: int
        """
