class Solution:
    def findLongestChain(self, pairs):
    
        pairs.sort(key=lambda x : x[0])
        res = [pairs[0]]

        for i in range(1, len(pairs)):
            if res[-1][1] < pairs[i][0]:
                res.append(pairs[i])
            else:
                if pairs[i][1] > res[-1][1]:
                    continue
                else:
                    res.pop()
                    res.append(pairs[i])

        return len(res)
