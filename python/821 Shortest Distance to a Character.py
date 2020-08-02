class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        res = [float('inf')] * n
        flag = False
        dist = 0
        for i in range(n):
            if S[i] == C:
                flag = True
                dist  = 0
            if flag:
                res[i] = dist
            dist += 1
        print(res)
        
        dist = 0
        flag = False
        for i in range(n-1, -1, -1):
            if S[i] == C:
                flag = True
                dist = 0
                
            if flag:
                res[i] = min(dist, res[i])
            dist += 1
        
        return res
        
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        res = []
        for i in range(n):
            if S[i] == C:
                res.append(0)
            else:
                l = i - 1
                r = i + 1
                dist = 1
                while l >= 0 or r < n:
                    if l >= 0 and S[l] == C:
                        res.append(dist)
                        break
                    elif r < n and S[r] == C:
                        res.append(dist)
                        break
                    else:
                        l -= 1
                        r += 1
                        dist += 1
        return res
                    
        
