#Time Limit
class Solution:
    def numSpecialEquivGroups(self, A):
        n = len(A)
        if n == 0: return 0
        res = []
        ans = []
        tmp2 = []
        
        def twoDic(dic, dic2):
            for i in range(len(dic)):
                if sorted(dic[i]) == sorted(dic2[i]):
                    continue
                else:
                    return False
            return True

        for i in range(n):
            if A[i] in tmp2:
                continue
            tmp = []
            tmp.append(A[i])
            dic = {}
            for k in range(len(A[i])):
                num = k % 2
                if num in dic:
                    dic[num].append(A[i][k])
                else:
                    dic[num] = [A[i][k]]

            dic2 ={}
            for j in range(i + 1, n):
                for k in range(len(A[j])):
                    num = k % 2
                    if num in dic2:
                        dic2[num].append(A[j][k])
                    else:
                        dic2[num] = [A[j][k]]
                if twoDic(dic, dic2):
                    tmp.append(A[j])
                    tmp2.append(A[j])
                dic2 = {}
            ans.append(tmp)
            tmp = []
        return len(ans)
        
#credit to: fuxuemingzhu
class Solution:
    def numSpecialEquivGroups(self, A):
        res = set()
        for i in A:
            res.add(''.join(sorted(i[0::2])) + ''.join(sorted(i[1::2])))
        return len(res)
