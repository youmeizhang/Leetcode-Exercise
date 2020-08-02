# credit to: http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-873-length-of-longest-fibonacci-subsequence/

class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [[2] * n for _ in range(n)]
        
        dic = {}
        for i in range(n):
            dic[A[i]] = i
        
        ans = 0
        for j in range(n):
            for k in range(j+1, n):
                diff = A[k] - A[j]
                if diff >= A[j]:
                    break
                if diff in dic:
                    i = dic[diff]
                    dp[j][k] = dp[i][j] + 1
                    ans = max(ans, dp[j][k])
                else:
                    continue

        return ans
  
