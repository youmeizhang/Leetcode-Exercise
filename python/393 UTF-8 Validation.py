class Solution(object):
    def validUtf8(self, data):
        n = len(data)
        i = 0
        def check(i, step, n):
            if i + step > n:
                return False
            for i in range(i + 1, i + step):
                if (data[i] >> 6) != 0b10:
                    return False
            return True

        while i < n:
            if (data[i] >> 3) == 0b11110:
                step = 4
            elif (data[i] >> 4) == 0b1110:
                step = 3
            elif (data[i] >> 5) == 0b110:
                step = 2
            elif (data[i] >> 7) == 0b0:
                step = 1
            else:
                return False
            if not check(i, step, n):
                return False
            i += step
        return True
