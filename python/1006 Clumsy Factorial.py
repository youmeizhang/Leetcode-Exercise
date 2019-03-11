#credit to: hanwang

class Solution(object):
    def clumsy(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N == 3:
            return 6
        if N == 4:
            return 7
        return N * (N - 1) // (N - 2) + N - 3 - self.helper(N - 4)

    def helper(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N == 3:
            return 6
        if N == 4:
            return 5
        return N * (N - 1) // (N - 2) - N + 3 + self.helper(N - 4)
        
# https://blog.csdn.net/fuxuemingzhu/article/details/88376892
class Solution(object):
    def clumsy(self, N):
        count = 0
        tmp = ""
        ops = ["*", "//", "+", "-"]

        for i in range(N,0,-1):
            if i != 1:
                tmp += str(i) + ops[count % 4]
            else:
                tmp += "1"
            count += 1

        return eval(tmp)
