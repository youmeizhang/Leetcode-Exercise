class Solution:
    def findAndReplacePattern(self, words, pattern):
        dic = {}
        tmp = []
        count = 1
        res = []
        for i in pattern:
            if i in dic:
                tmp.append(dic[i])
            else:
                tmp.append(count)
                dic[i] = count
                count += 1
        
        dic2 = {}
        tmp2 = []
        count = 1
        for i in words:
            for j in i:
                if j in dic2:
                    tmp2.append(dic2[j])
                else:
                    tmp2.append(count)
                    dic2[j] = count
                    count += 1
                          
            if tmp == tmp2:
                res.append(i)
            count = 1
            dic2 = {}
            tmp2 = []
            
        return res
