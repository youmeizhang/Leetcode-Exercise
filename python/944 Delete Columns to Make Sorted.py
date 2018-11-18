class Solution(object):
    def minDeletionSize(self, A):
        count = 0
        for i in range(len(A[0])): # the indice of the char in a string
            for j in range(1, len(A)):
                if ord(A[j][i]) >= ord(A[j-1][i]):
                    continue
                else:
                    count += 1
                    break
        return count
