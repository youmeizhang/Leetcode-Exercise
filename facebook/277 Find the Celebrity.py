# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        k = 0
        for i in range(n):
            k = k if knows(i, k) else i
            
        for i in range(n):
            if i != k and (not knows(i, k) or knows(k, i)):
                return -1
        return k
                
        """
        :type n: int
        :rtype: int
        """
        
