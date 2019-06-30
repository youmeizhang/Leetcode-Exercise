class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        n = len(S)
        if n < K:
            return 0
        count = 0
        for i in range(n-K+1):
            tmp = S[i:i+K]
            if len(set(tmp)) == len(tmp):
                count += 1
        return count
        
