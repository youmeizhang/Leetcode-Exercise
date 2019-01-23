class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        point = [p1, p2, p3, p4]
        res = []
        for i in range(len(point)):
            for j in range(i+1, len(point)):
                tmp = (point[i][0] - point[j][0]) ** 2 + (point[i][1] - point[j][1]) ** 2
                if tmp == 0:
                    return False
                res.append(tmp)

        dic = collections.Counter(res)
        res = list(set(res))
        if len(res) != 2:
            return False
        if 2 * dic[res[0]] == dic[res[1]] or 2 * dic[res[1]] == dic[res[0]]:
            return True
        return False
