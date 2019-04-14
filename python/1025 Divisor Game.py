class Solution(object):
    def divisorGame(self, N):
        count = 0
        while N > 1:
            for i in range(1, N):
                if N % i == 0:
                    N = N - i
                    count += 1
                    break

            if i == N - 1: 
                if N % i == 0:
                    N = N - i
                    count += 1
                break

        if count % 2 == 1:
            return True
        else:
            return False
        """
        :type N: int
        :rtype: bool
        """
