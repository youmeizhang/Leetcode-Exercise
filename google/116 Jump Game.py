class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        dp = [False for _ in range(len(A))]
        dp[0] = True
        
        for i in range(1, len(A)):
            for j in range(i):
                if dp[j] and A[j] + j >= i:
                    dp[i] = True
                    break

        return dp[-1]
    
 class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        reach = 0
        for i in range(len(A)):
            if i > reach:
                return False
            reach = max(reach, i + A[i])
        return True
