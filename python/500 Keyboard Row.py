class Solution:
    def findWords(self, words):
        first = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        second = ['a', 's', 'd','f','g','h','j','k','l']
        third = ['z','x','c','v','b','n','m']
        res = []
        for word_old in words:
            word = word_old.lower()
            if word[0] in first:
                idx = first
            elif word[0] in second:
                idx = second
            elif word[0] in third:
                idx = third
                
            for i in range(len(word)):
                if word[i] not in idx:
                    break
                elif i == len(word) - 1:
                    res.append(word_old)
                else:
                    continue
        return res
