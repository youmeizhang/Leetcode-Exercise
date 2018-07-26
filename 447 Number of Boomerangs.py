class Solution:
    def numberOfBoomerangs(self, points):
        res = 0
        n = len(points)
        if n < 3: return res
        for x1, y1 in points:
            dic = collections.defaultdict(int)
            for x2, y2 in points:
                dis = (x1-x2) ** 2 + (y1-y2) ** 2
                dic[dis] += 1
            for i in dic:
                if i != 0:
                    tmp = dic[i] * (dic[i] - 1)
                    res += tmp
        return res
