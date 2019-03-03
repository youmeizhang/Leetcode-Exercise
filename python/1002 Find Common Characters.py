class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = A[0]
        
        for i in range(1, len(A)):
            tmp = []
            dic = collections.Counter(res)

            for ele in A[i]:
                if ele in dic and dic[ele] != 0:

                    tmp.append(ele)
                    dic[ele] -= 1
            res = tmp

        return res

            
        
