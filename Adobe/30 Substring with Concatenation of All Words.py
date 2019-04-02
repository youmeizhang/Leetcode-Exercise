class Solution(object):
    def findSubstring(self, s, words):
        if s == "" or words == []:
            return ''
        total = len(words) * len(words[0])
        sn = len(words[0])
        n = len(s)
        res = set()
        flag = False
        dic = collections.Counter(words)
        for i in range(n - total + 1):
            if s[i:i+sn] in words:
                sub_s = s[i:i+total]
                sub_s_split = list(map(''.join, zip(*[iter(sub_s)] * sn)))
                tmp = collections.Counter(sub_s_split)

                for j in range(len(sub_s_split)):
                    if sub_s_split[j] in words and tmp == dic:                    
                        res.add(i)

        return list(res)
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
