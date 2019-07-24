class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        #print(v1, v2)
        n = len(v1)
        m = len(v2)
        
        for i in range(min(n, m)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
            else:
                continue
                
        if m > n:
            for j in range(n, m):
                if int(v2[j]) != 0:
                    return -1
            return 0
        elif m == n:
            return 0
        elif m < n:
            for j in range(m, n):
                if int(v1[j]) != 0:
                    return 1
            return 0
