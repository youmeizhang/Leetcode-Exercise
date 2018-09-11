class Solution:
    def leastBricks(self, wall):
        n = len(wall)
        last_brick = sum(wall[0])
        dic = {}
        for i in range(n):
            m = len(wall[i])
            summ = 0
            for j in range(m):
                summ += wall[i][j]
                if summ != last_brick:
                    if summ in dic:
                        dic[summ] += 1
                    else:
                        dic[summ] = 1
                else:
                    continue
        return len(wall) - max(dic.values()) if dic else len(wall)
