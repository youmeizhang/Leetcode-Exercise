class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        n = len(customers)
        total = 0

        for i in range(n):
            if grumpy[i] == 0:
                total += customers[i]
                customers[i] = 0

        sum_ = sum(customers[:X])

        res = max(sum_, 0)
        for i in range(X, n):
            sum_ -= customers[i - X]
            sum_ += customers[i]
            res = max(sum_, res)

        return max(res, sum_) + total
            
            
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        
