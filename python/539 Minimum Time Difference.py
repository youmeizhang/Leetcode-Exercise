class Solution:
    def findMinDifference(self, timePoints):
        l1 = [w.replace('00:00', '24:00') for w in timePoints]
        l1 = list(sorted(l1))  
        first = str(int(l1[0].split(':')[0]) + 24) + l1[0][2:]
        l1.append(first)
        n = len(l1)
        res = float('inf')
        for i in range(1, n):
            cur = 0
            tmp = int(l1[i].split(":")[1])
            if tmp == 0:
                tmp = 60
                cur = -1
            minute = tmp - int(l1[i - 1].split(":")[1])
            hour = int(l1[i].split(":")[0]) - int(l1[i - 1].split(":")[0]) + cur
            res = min(res, hour * 60 + minute)
        return res
