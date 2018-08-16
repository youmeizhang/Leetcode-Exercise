class Solution:
    def findAnagrams(self, s, p):
        n = len(s)
        m = len(p)
        dic = collections.Counter(p)
        dic2 = collections.Counter()
        res = []
        for i in range(n):
            dic2[s[i]] += 1
            if i >= m:
                dic2[s[i - m]] -= 1
                if dic2[s[i-m]] == 0:
                    del dic2[s[i - m]]
            if dic2 == dic:
                res.append(i - m + 1)
        return res
        

#time limit
class Solution:
    def findAnagrams(self, s, p):
        n = len(s)
        m = len(p)
        dic = collections.Counter(p) # be careful about using regular dict, if there is no key in dict, raise error
        dic2 = collections.Counter(p)
        res = []
        for i in range(n- m + 1):
            for j in range(i, i + m):
                if (dic2[s[j]] != None):
                    dic2[s[j]] -= 1
            if all(value == 0 for value in dic2.values()):
                res.append(i)
            dic2 = collections.Counter(p)
        return res
