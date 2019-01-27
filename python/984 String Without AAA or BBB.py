class Solution(object):
    def strWithout3a3b(self, A, B):
        flag = False
        s = ""

        if A < B:
            tmp = A
            A = B
            B = tmp
            flag = True

        numaa = A // 2
        numa = A - numaa * 2
        a_list = ["xx"] * numaa + ["x"] * numa 
        spacea = len(a_list) - 1

        numb = spacea 
        numbb = B - spacea

        new_numb = numb - numbb

        if numbb * 2 > B:
            numbb = 0
            new_numb = B

        b_list = ["yy"] * numbb + ["y"] * new_numb

        lenb = len(b_list)
        lena = len(a_list)

        if lenb > lena + 1:
            new_b_list = b_list[:2*lena - lenb] + ["yy"] * (lenb - lena)
        else:
            new_b_list = b_list

        while a_list or new_b_list:
            if a_list:
                s += a_list.pop(0)
            if b_list:
                s += new_b_list.pop(0)
        if a_list:
            s += a_list.pop(0)
        if new_b_list:
            s += new_b_list.pop(0)

        if not flag:
            s = s.replace("x", "a")
            s = s.replace("y", "b")
            return s
        else:
            s = s.replace("x", "b")
            s = s.replace("y", "a")
            return s

#credit to: fuxuemingzhu 
class Solution(object):
    def strWithout3a3b(self, A, B):
        a, b = ("a", "b") if A > B else ("b", "a")
        A, B = (A, B) if A > B else (B, A)
        
        ab = [a+b] * B
        A -= B
        res = []
        while A:
            res.append(a)
            if ab:
                res.append(ab.pop())
            A -= 1
        res += ab
        return "".join(res)
