class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = {}
        n = len(S)
        for i in range(n):
            dic[S[i]] = i
        res = []
        start = 0
        end = 0
        for i in range(n):
            if dic[S[i]] > end:
                end = dic[S[i]]
            if i >= end:
                res.append(end - start + 1)
                start = end + 1
                
        return res
            
        
