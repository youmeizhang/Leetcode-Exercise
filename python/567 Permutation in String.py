class Solution(object):
    def checkInclusion(self, s1, s2):
        def isPermute(s1, s2):
            if len(s1) != len(s2):
                return False
            dic1 = {}
            dic2 = {}

            for i in range(len(s1)):
                if s1[i] in dic1:
                    dic1[s1[i]] += 1
                else:
                    dic1[s1[i]] = 1
                if s2[i] in dic2:
                    dic2[s2[i]] += 1
                else:
                    dic2[s2[i]] = 1
            return dic1 == dic2
        
        n2 = len(s2)
        n1 = len(s1)

        for i in range(n2):
            tmp = s2[i:i+n1]
            if isPermute(s1, tmp):
                return True
        return False
