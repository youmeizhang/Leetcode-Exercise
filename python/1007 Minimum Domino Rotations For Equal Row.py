class Solution(object):
    def minDominoRotations(self, A, B):
        a = max(((item, A.count(item)) for item in set(A)), key=lambda a: a[1])[0]
        b = max(((item, B.count(item)) for item in set(B)), key=lambda a: a[1])[0]
        count1 = 0

        flag1 = False
        flag2 = False

        for i in range(len(A)):
            if A[i] != a and B[i] != a:
                break
            elif i == len(A) - 1 and (A[i] == a or B[i] == a):
                flag1 = True
                if A[i] != a and B[i] == a:
                    count1 += 1
            elif A[i] != a and B[i] == a:
                count1 += 1
            else:
                continue

        count2 = 0
        for i in range(len(B)):
            if B[i] != b and A[i] != b:
                break
            elif i == len(B) - 1 and (B[i] == b or A[i] == b):
                flag2 = True
                if B[i] != b and A[i] == b:
                    count2 += 1
            elif B[i] != b and A[i] == b:
                count2 += 1
            else:
                continue

        if flag1 and flag2:
            return min(count1, count2)
        if flag1:
            return count1
        if flag2:
            return count2

        return -1
