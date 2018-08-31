class Solution:
    def convertToBase7(self, num):
        sign = ''
        if num * -1 > 0:
            num = num * -1
            sign = '-'
        i = num % 7
        j = num // 7
        res = str(i)
        while(j != 0):
            i = j % 7
            j = j // 7
            res += str(i)
        res += sign
        return res[::-1]
