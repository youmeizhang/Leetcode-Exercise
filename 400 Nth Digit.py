class Solution(object):
    def findNthDigit(self, n):
        for i in range(9):
            tmp = 9 * 10 ** i
            if n <= tmp * (i + 1):
                break
            n -= tmp * (i + 1)
        n -= 1
        res = int(str(10**i + n / (i + 1))[n % (i + 1)])
        return res
