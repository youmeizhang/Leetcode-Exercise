class Solution(object):
    def multiply(self, num1, num2):
        t1 = 0
        for i in range(len(num1)):
            t1 = t1 * 10 + int(num1[i])

        t2 = 0
        for j in range(len(num2)):
            t2 = t2 * 10 + int(num2[j])

        return str(t1 * t2)
