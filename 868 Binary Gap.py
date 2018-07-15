class Solution(object):
    def binaryGap(self, N):
        bi = "{0:b}".format(N)
        n = len(bi)
        pos = []
        for i in range(n):
            if bi[i] == '1':
                pos.append(i)
        max_value = 0
        m = len(pos)
        for i in range(1, m):
            max_value = max(max_value, (pos[i] - pos[i-1]))
        return max_value    
