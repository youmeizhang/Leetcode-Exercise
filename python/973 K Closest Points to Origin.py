class Solution(object):
    def kClosest(self, points, K):
        dic = {}
        for point in points:
            d = (abs(point[0]))**2 + (abs(point[1]))**2
            dic[d] = point

        sorted_x = sorted(dic.items(), key = operator.itemgetter(0))

        ans = []
        for i in range(K):
            ans.append(sorted_x[i][1])

        return ans 
