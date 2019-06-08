# credit to: https://blog.csdn.net/wilzxu/article/details/90746272

class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        res = 0

        presum = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j != 0:
                    presum[i][j] = matrix[i][j] + presum[i][j-1]
                else:
                    presum[i][j] = matrix[i][j]

        for l in range(n):
            for r in range(l, n):
                rowsum = [0] * m
                dic = {}
                dic[0] = 1
                sum_ = 0
                for i in range(m):
                    if l != 0:
                        rowsum[i] = presum[i][r] - presum[i][l-1]
                    else:
                        rowsum[i] = presum[i][r]

                    sum_ += rowsum[i]
                    if (sum_ - target) in dic:
                        res += dic[sum_ - target]
                        
                    if sum_ in dic:
                        dic[sum_] += 1
                    else:
                        dic[sum_] = 1
        return res
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
