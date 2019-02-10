class Solution:
    def addBoldTag(self, s: 'str', dic: 'List[str]') -> 'str':
        bold = [False for _ in range(len(s))]
        for i in range(len(s)):    
            for part in dic:
                if s[i:i + len(part)] == part:
                    for j in range(i, i + len(part)):
                        bold[j] = True

        res = ""
        for j in range(len(bold)):
            if j < 1:
                if bold[j]:
                    res += "<b>"
                    res += s[j]
                else:
                    res += s[j]
            else:
                if bold[j-1] and not bold[j]:
                    #true false
                    res += "</b>"
                    res += s[j]
                elif not bold[j-1] and bold[j]:
                    #false true
                    res += "<b>"
                    res += s[j]
                else:
                    #true true
                    res += s[j]

        if bold[-1]:
            res += "</b>"
        return res


