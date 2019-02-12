class Solution:
    """
    @param s: the long string
    @param word: the secrect word
    @return: whether a substring exists in the string can be transformed by the above encoding rule
    """
    def getAns(self, s, word):
        # Write a code here
        dic_word = collections.Counter(word)
        key_word = dic_word.values()
        
        for i in range(len(s) - len(word)):
            tmp = s[i:i+len(word)]
            
            dic_s = collections.Counter(tmp)
            key_s = dic_s.values()
            
            if sorted(key_word) == sorted(key_s):
                return "yes"
        
        return "no"
