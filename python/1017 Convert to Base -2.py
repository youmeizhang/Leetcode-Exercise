class Solution(object):
    def baseNeg2(self, N):
        if N == 0:
            return '0'
        converted = ''
        while N != 0:
            remainder = N % (-2)
            N = int(N // (-2))
            if remainder < 0:
                remainder += ((-1) * (-2))
                N += 1
            converted = str(remainder) + converted
        return converted
        """
        :type N: int
        :rtype: str
        """
        
