class Solution(object):
    def sortedSquares(self, A):
        return sorted(list(map(lambda x: x**2, A)))
