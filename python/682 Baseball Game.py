class Solution(object):
    def calPoints(self, ops):
        n = len(ops)
        res = []
        for i in range(n):
            if ops[i].isdigit() or '-' in ops[i]:
                res.append(int(ops[i]))
            elif ops[i] == 'C':
                k = i - 1
                while k >= 0 and res[k] == 'invalid':
                    k -= 1
                res[k] = 'invalid'
                res.append('invalid')

            elif ops[i] == 'D':
                pos = i - 1
                while pos >= 0 and res[pos] == 'invalid':
                    pos -= 1

                res.append(res[pos] * 2)
            elif ops[i] == '+':
                x = i - 1
                while x > 0 and res[x] == 'invalid':
                    x -= 1
                y = x - 1
                while y >= 0 and res[y] == 'invalid':
                    y -= 1
                res.append(int(res[x]) + int(res[y]))

        total = 0
        for char in res:
            if isinstance(char, int):
                total += int(char)
            else:
                continue
        return total
