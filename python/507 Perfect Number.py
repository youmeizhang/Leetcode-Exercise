class Solution:
    def checkPerfectNumber(self, num):
        if not num: return False
        if num == 1: return False
        res = [1]
        if num < 0:
            return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                res.append(i)
                res.append(int(num / i))
            else:
                continue
        return num == sum(res)
