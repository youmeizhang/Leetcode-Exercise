class Solution(object):
    def fractionAddition(self, expression):
        def gcd(a, b):
            flag = 1
            if a * b < 0:
                a = abs(a)
                b = abs(b)
                flag = -1

            res = 1
            smaller = a if a < b else b
            for i in range(1, smaller + 1):
                if a % i == 0 and b % i == 0:
                    res = i
            return res * flag

        exp = []
        start = 0
        end = 0

        for i in range(len(expression)):
            if expression[i] == "-" and i == 0:
                start = 0
            elif expression[i] == "-":
                end = i
                exp.append(expression[start:end])
                start = i
            elif expression[i] == "+":
                end = i
                exp.append(expression[start:end])
                start = i+1
            else:
                continue

        exp.append(expression[start:])


        res = "0/0"

        flaga = 1
        flagb = 1

        for i in range(len(exp)):
            if exp[i][0] == "-":
                a = exp[i][1:]
                flaga = -1
                if res[0] == "-":
                    b = res[1:]
                    flagb = -1
                else:
                    b = res
            else:
                a = exp[i]
                if res[0] == "-":
                    b = res[1:]
                    flagb = -1
                else:
                    b = res
    
            if int(b.split("/")[1]) != 0:
                mole = flaga * int(a.split("/")[0]) * int(b.split("/")[1]) + flagb * int(b.split("/")[0]) * int(a.split("/")[1])
                deno = int(a.split("/")[1]) * int(b.split("/")[1])
            else:
                mole = flaga * int(a.split("/")[0])
                deno = int(a.split("/")[1])

            tmp = gcd(mole, deno)
            mole = mole // tmp
            deno = deno // tmp

            if mole * deno > 0:
                res = str(abs(mole)) + "/" + str(abs(deno))

            elif mole * deno == 0:
                res = "0/0"

            else:
                if deno < 0:
                    res = str(-1 * mole) + "/" + str(-1 * deno)
                else:
                    res = str(mole) + "/" + str(deno)

            flaga = 1
            flagb = 1

        if res[0] == "-":
            if res[1] == "0":
                return "0/1"
            else:
                return res
        elif res[0] == "0":
                return "0/1"
        else:
            return res      
