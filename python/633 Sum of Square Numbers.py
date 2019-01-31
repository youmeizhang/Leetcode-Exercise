class Solution:
    def judgeSquareSum(self, c):
        deno = int(math.sqrt(c))
        for i in range(deno+1):
            if math.sqrt(c - i**2).is_integer():
                return True
            else:
                continue
        return False
