class Solution(object):
    def countTriplets(self, A):
        res = 0
        n = len(A)
        dic = collections.defaultdict(list)
        
        for i in range(0, n):
            for j in range(0, n):
                tmp = A[i] & A[j]
                if tmp not in dic:
                    dic[tmp] = 1
                else:
                    dic[tmp] += 1
           
        for k in range(0, n):
            for i, key in enumerate(dic):
                if key & A[k] == 0:
                    res += dic[key]
                else:
                    continue
            
        return res
