class Solution(object):
    def lemonadeChange(self, bills):
        dic = {5:0, 10:0, 20:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                dic[5] += 1
            elif bills[i] == 10:
                dic[10] += 1
                dic[5] -= 1
                if dic[5] < 0:
                    return False
            elif bills[i] == 20:
                dic[20] += 1
                if dic[5] >= 1 and dic[10] >= 1:
                    dic[5] -= 1
                    dic[10] -= 1
                elif dic[5] >= 3:
                    dic[5] -= 3
                else:
                    return False
        return True
