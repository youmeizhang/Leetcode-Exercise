class Solution(object):
    def removeKdigits(self, num, k):
        n = len(num)
        dic = collections.defaultdict(collections.deque)
        for i, v in enumerate(num):
            dic[v].append(i)
        p = 0
        ans = '0'
        for x in range(n - k):
            for y in '0123456789':
                while dic[y] and dic[y][0] < p:
                    dic[y].popleft()
                if dic[y] and dic[y][0] <= k + x:
                    p = dic[y][0]
                    ans += y
                    dic[y].popleft()
                    break
        return str(int(ans))
