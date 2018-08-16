class Solution(object):
    def reorderedPowerOf2(self, N):
        if N == 1: return True
        out = [ 2**j for j in range(1,30) ]
        ref = {}

        for i in out:
            n = len(str(i))
            if n in ref:
                ref[n].append(i)
            else:
                ref[n] = [i]

        tmp = {}
        for i in str(N):
            if i in tmp:
                tmp[i] += 1
            else:
                tmp[i] = 1

        n = len(str(N))

        tmp2 = {}
        if n in ref:
            for i in ref[n]:
                for j in str(i):
                    if j in tmp2:
                        tmp2[j] += 1
                    else:
                        tmp2[j] = 1

                if tmp2 == tmp:
                    return True
                tmp2 = {}
            return False
