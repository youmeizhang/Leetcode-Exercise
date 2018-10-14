class Solution:
    def sortArrayByParityII(self, A):
        res = [0] * len(A)
        
        #even = []
        #odd = []
        
        even = 0
        odd = 1
        
        for i in A:
            if i % 2 == 0:
                res[even] = i
                even += 2
            else:
                res[odd] = i
                odd += 2
                
        return res
