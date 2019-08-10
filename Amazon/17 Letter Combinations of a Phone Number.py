class Solution(object):
    def letterCombinations(self, digits):
        dict = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        
        def recursion(res, string, index):
            if index == len(digits):
                if string != "":
                    res.append(string)
                return res
            for i in range(len(dict[digits[index]])):
                recursion(res, string + dict[digits[index]][i], index + 1)
        
        res = []
        recursion(res, '', 0)
        return res
            
            
        
        """
        :type digits: str
        :rtype: List[str]
        """
        
