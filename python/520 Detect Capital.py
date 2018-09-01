class Solution:
    def detectCapitalUse(self, word):
        if not word: return True

        def secondword(word):
            for i in range(1, len(word)):
                if 'a' <= word[i] <= 'z':
                    continue
                else: 
                    return False
            return True

        if 'A' <= word[0] <= 'Z':
            for i in word:
                if 'A' <= i <= 'Z':
                    continue
                elif secondword(word):
                    return True
                else:
                    return False
            return True

        if 'a' <= word[0] <= 'z':
            for i in word:
                if 'a' <= i <='z':
                    continue
                else:
                    return False
            return True
        return False 
