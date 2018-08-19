#failed
class Solution:
    def findAndReplacePattern(self, words, pattern):
        n = len(words)
        dic = defaultdict(int)
        p = defaultdict(int)
        tmp = []
        tmp2 = []
        ans = []
        for k in pattern:
            if k not in p:
                p[k] = 1
            else:
                p[k] += 1
        tmp2 = list(p.values())
        print(tmp2)
        for i in range(n):
            for j in words[i]:
                if j in dic:
                    dic[j] += 1
                else:
                    dic[j] = 1
            tmp = list(dic.values())
            print(tmp)
            if tmp == tmp2:
                ans.append(words[i])
            dic = defaultdict(int)
        return ans
        
