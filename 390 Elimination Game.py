#time limited

class Solution(object):
    def lastRemaining(self, n):
        a = list(range(1, n+1))
        cnt = 0
        while (len(a) > 1):
            if cnt % 2 == 0:
                a = [a[i] for i, v in enumerate(a) if i % 2 == 1]
                cnt += 1
                a = list(reversed(a))
            else:
                a = [a[i] for i, v in enumerate(a) if i % 2 == 1]
                a = list(reversed(a))
                cnt += 1
        return a[0]
