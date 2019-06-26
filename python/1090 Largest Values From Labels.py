class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        dic = {}
        n = len(values)
        for i in range(n):
            if labels[i] in dic:
                dic[labels[i]].append(values[i])
            else:
                dic[labels[i]] = [values[i]]
        l = []
        for i, key in enumerate(dic):
            tmp = list(sorted(dic[key], reverse = True))
            l += tmp[:use_limit]

        res = list(sorted(l,reverse = True))
        return sum(res[:num_wanted])
        
