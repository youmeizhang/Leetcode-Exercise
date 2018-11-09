def closest(s, queries):
    # Write your code here
    if s == "":
        return [-1] * len(queries)
    if queries == []:
        return []
    dic = {}
    for i in range(len(s)):
        if s[i] in dic:
            dic[s[i]].append(i)
        else:
            dic[s[i]] = [i]
    res = []
    for i in queries:
        try:
            if s[i] in dic:
                tmp = dic[s[i]]
                if len(tmp) < 2:
                    res.append(-1)
                else:
                    tmp = sorted(tmp)
                    idx = tmp.index(i)
                    if idx == len(tmp) - 1:
                        res.append(tmp[idx-1])
                    else:
                        if tmp[idx-1] > tmp[idx+1]:
                            res.append(tmp[idx+1]) 
                        else:
                            res.append(tmp[idx-1])
        except:
            res.append(-1)
    return res
