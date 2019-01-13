class Solution(object):
    def subarraysDivByK(self, A, K):
        n = len(A)
        mod =[] 
        for i in range(K + 1): 
            mod.append(0) 
        cumSum = 0
        for i in range(n): 
            cumSum = cumSum + A[i] 
            mod[((cumSum % K)+K)% K]= mod[((cumSum % K)+K)% K] + 1


        result = 0

        for i in range(K): 
            if (mod[i] > 1): 
                result = result + (mod[i]*(mod[i]-1))//2

        result = result + mod[0] 

        return result 
