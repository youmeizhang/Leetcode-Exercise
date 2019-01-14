#time limit (1)
class Solution(object):
    def oddEvenJumps(self, A):
        higher = [1] * len(A)
        lower = [1] * len(A)
        i = len(A) - 2
        while i >= 0:
            tmp = A[i+1:]
            try:
                largest_min = max(x for x in tmp if x <= A[i])
                if largest_min != -1:
                    j = tmp.index(largest_min) + i
                    lower[i] = higher[j + 1]
            except:
                lower[i] = 0

            try:
                smallest_max = min(x for x in tmp if x >= A[i])
                if smallest_max != -1:
                    p = tmp.index(smallest_max) + i
                    higher[i] = lower[p + 1]
            except:
                higher[i] = 0
            i -= 1
        return sum(higher)
    
#time limit (2)   
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

#credit to author: lee215
class Solution(object):
    def oddEvenJumps(self, A):
        n = len(A)
        next_higher = [0] * n
        next_lower = [0] * n

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher = [0] * n
        lower = [0] * n

        higher[-1] = 1
        lower[-1] = 1

        for i in range(len(A) - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]

        return sum(higher)
