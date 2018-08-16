class Solution(object):
    def integerReplacement(self, n):
        cnt = 0
        while(n > 1):
            if n % 2 == 1:
                if (n + 1) % 4 == 0 and n != 3 and n != 7:
                    n = n + 1
                    cnt += 1
                else:
                    n = n - 1
                    cnt += 1
            else:
                n = n / 2
                cnt += 1
        return cnt
