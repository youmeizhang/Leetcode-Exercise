class Solution(object):
    def lengthLongestPath(self, input):
        dic = {0:0}
        maxlen = 0
        for i in input.splitlines():
            name = i.lstrip("\t")
            cnt = len(i) - len(name)
            if '.' in name:
                maxlen = max(len(name) + dic[cnt], maxlen)
            else:
                dic[cnt + 1] = dic[cnt] + len(name) + 1
        return maxlen
