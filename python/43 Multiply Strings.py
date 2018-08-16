class Solution(object):
    def multiply(self, num1, num2):
        n = len(num1)
        m = len(num2)
        res = []
        tmp = 0
        position = 1
        carry = 0
        result = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        tmp_list = ''
        result = 0
        for i in range(n):
            for j in range(m):
                tmp = (int(num1[i]) * int(num2[j]) + carry)
                carry = tmp // 10
                a = tmp % 10
                tmp_list += str(a)
            if carry != 0:
                tmp_list += str(carry)

            res.append(tmp_list[::-1])
            tmp = 0
            carry = 0
            tmp_list = ''

        for i in range(len(res)):
            result += int(res[i]) * position
            position *= 10
        return str(result)
