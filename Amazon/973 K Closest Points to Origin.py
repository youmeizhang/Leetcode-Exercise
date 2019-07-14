class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dic = {}
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            if dist in dic:
                dic[dist].append(point)
            else:
                dic[dist] = [point]
            
        point = sorted(dic)

        res = []
        cnt = 0
        for i in range(min(len(point), K)):
            tmp = dic[point[i]]
            
            for p in tmp: 
                if cnt < K:
                    res.append(p)
                    cnt += 1
                else:
                    return res
        return res
        
