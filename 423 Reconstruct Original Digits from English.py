class Solution(object):
    def originalDigits(self, s):
        dic = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}            
        for i in s:
            if i == 'z': dic[0] += 1
            elif i == 'w': dic[2] += 1
            elif i == 'u': dic[4] += 1
            elif i == 'x': dic[6] += 1
            elif i == 'g': dic[8] += 1

            elif i == 's': dic[7] += 1
            elif i == 'f': dic[5] += 1
            elif i == 'h': dic[3] += 1
            elif i == 'i': dic[9] += 1
            elif i == 'o': dic[1] += 1

        dic[7] -= dic[6]
        dic[5] -= dic[4]
        dic[3] -= dic[8]
        dic[1] = dic[1] - dic[0] - dic[2] - dic[4]
        dic[9] = dic[9] - dic[5] - dic[6] - dic[8]
        res = []
        for i in dic:
            if dic[i] != 0:
                res += dic[i] * [i]
        res.sort()        
        return "".join(str(i) for i in res)
