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
                    
        
