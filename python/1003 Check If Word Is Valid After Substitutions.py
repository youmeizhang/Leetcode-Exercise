class Solution:
    def isValid(self, S: str) -> bool:
        dic = collections.Counter(S)
        #print(dic["a"], dic["b"], dic["c"])
        if len(set(S)) != 3:
            return False

        if dic["a"] != dic["b"] or dic["a"] != dic["c"]:
            return False

        if dic["a"] == 0 or dic["b"] == 0 or dic["c"] == 0:
            return False

        numa = 0
        numb = 0
        numc = 0

        for i in range(len(S)):
            if S[i] == "a":
                numa += 1
            if S[i] == "b":
                numb += 1
            if S[i] == "c":
                numc += 1

            if numc > numa:
                return False

            if numc > numb:
                return False
            if numb > numa:
                return False
        return True
