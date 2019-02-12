class Solution:
    """
    @param a: the points
    @return: return the maximum rectangle area
    """
    def getMaximum(self, a):
        # write your code here
        dic = {}
        for ele in a:
            if ele[0] in dic:
                if ele[1] not in dic[ele[0]]:
                    dic[ele[0]].append(ele[1])
                else:
                    continue
            else:
                dic[ele[0]] = [ele[1]] 
            
        res = 0
        keys = dic.keys()
        for i, key in enumerate(dic):
            for p in range(len(dic[key])):
                for q in range(p + 1, len(dic[key])):
                    y1 = dic[key][p]
                    y2 = dic[key][q]
                    
                    for x in keys:
                        if x == key:
                            continue
                        else:
                            if y1 in dic[x] and y2 in dic[x]:
                                total = abs(x - key) * abs(y2 - y1)
                                res = max(res, total)
        
        return res
