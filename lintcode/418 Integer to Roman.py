class Solution:
    """
    @param n: The integer
    @return: Roman representation
    """
    def intToRoman(self, n):
        # write your code here
        res = ""
        num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        for i in range(len(num)):
            if n < num[i]:
                continue
            while n >= num[i]:
                n -= num[i]
                res += roman[i]
                
        return res
