class Solution:
    def isNumber(self, s: 'str') -> 'bool':
        try:
            if float(s) == 0.0 or float(s) or int(s):
                return True
        except:
            count = 0
            for i in range(len(s)):
                if s[i].isalpha():
                    if s[i] != "e":
                        return False
                    else:
                        try:
                            int(s[i+1:])
                        except:
                            return False
                        try:
                            former = s[:i].replace(" ", "")
                            if former == "":
                                return False
                        except:
                            return False
                elif s[i].isdigit():
                    if int(s[i]) >= 0 and int(s[i]) <= 9:
                        continue

                elif s[i] == "+" or s[i] == "-":
                    if i > 0 and i < len(s) - 1:
                        if s[i-1] == "+" or s[i-1] == "-" or s[i+1] == "+" or s[i+1] == "-":
                            return False
                        elif s[i-1] != "e":
                            return False
                    elif i == len(s) - 1:
                        return False
                elif s[i] == ".":
                    count += 1
                    if count > 1:
                        return False
                    if i > 0 and i < len(s) - 1:
                        if not s[i-1].isdigit() or not s[i+1].isdigit():
                            return False
                    elif i == 0 or i == len(s) - 1:
                        return False
                else:
                    return False
        return True
        
#using Regular Expression
#credit to: https://leetcode.com/problems/valid-number/discuss/234911/Use-regex

import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return re.search("^([+-])?((\d+(\.\d*)?)|(\.\d+))(e[+-]?\d+)?$", s.strip()) is not None
