#time limit
class Solution(object):
    def oddEvenJumps(self, A):
        res = 1
        for i in range(len(A) - 1):
            original = i
            count = 1
            #print("starting round: ", original)
            while i < len(A) - 1:
                if max(A[i+1:]) >= A[i] and count % 2 == 1:
                    tmp = A[i+1:]
                    smallest_max = min(x for x in tmp if x >= A[i])
                    j = tmp.index(smallest_max)
                    i = i + j + 1
                    #print("1. jump i to: ", i)
                    count += 1
                elif min(A[i+1:]) <= A[i] and count % 2 == 0:
                    tmp = A[i+1:]
                    largest_min = max(x for x in tmp if x <= A[i])
                    j = tmp.index(largest_min)
                    i = i + j + 1
                    #print("2. jump i to: ", i)
                    count += 1
                else:
                    break
            if i == len(A) - 1:
                res += 1
            i = original
        return res
