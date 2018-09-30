class Solution:
    def hasGroupsSizeX(self, deck):
        dic = collections.Counter(x for x in deck)
        occu = []

        for i in dic:
            occu.append(dic[i])

        occu = set(occu)
        min_value = min(occu)
        if min_value < 2:
            return False
        for i in occu:
            if  self.gcd(i, min_value) == 1:
                return False
        return True

    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        while b != 0:
            tmp = a% b
            a = b
            b = tmp
        return a
