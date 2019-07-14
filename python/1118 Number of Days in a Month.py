class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        a = [1, 3, 5, 7, 8, 10, 12]
        b = [4, 6, 9, 11]
        if M in a:
            return 31
        elif M in b:
            return 30
        elif Y % 100 == 0 and M == 2:
            if Y % 400 == 0:
                return 29
            else:
                return 28
        elif Y % 4 == 0 and M == 2:
            return 29
        else:
            return 28
        
        
            
        
