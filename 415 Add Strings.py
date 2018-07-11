class Solution(object):
    def addStrings(self, num1, num2):
        n = len(num1)
        m = len(num2)
        res = []
        carry = 0
        while n or m or carry:
            tmp = carry
            if n:
                n -= 1
                tmp += int(num1[n])
            if m:
                m -= 1
                tmp += int(num2[m])
            carry = tmp > 9
            res.append(str(tmp % 10))
        return ''.join(res[::-1])
