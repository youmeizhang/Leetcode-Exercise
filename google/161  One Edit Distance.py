class Solution:
    def isOneEditDistance(self, s: 'str', t: 'str') -> 'bool':
        if len(s) == len(t):
            # can only replace a char
            if len(s) == 0:
                return False
            for i in range(len(s)):
                if s[i] != t[i]:
                    if s[i+1:] == t[i+1:]:
                        return True
                    else:
                        return False
            return True if s != t else False
        
        elif len(s) > len(t):
            # delete one char
            if t == "":
                if len(s) - len(t) == 1:
                    return True
                else:
                    return False

            for i in range(len(t)):
                if s[i] != t[i]:
                    if s[i+1:] == t[i:]:
                        return True
                    else:
                        return False

            return True if len(s) - len(t) == 1 else False

        elif len(s) < len(t):
            #insert one char
            if len(s) == 0:
                if len(t) - len(s) == 1:
                    return True
                else:
                    return False

            for i in range(len(s)):
                if s[i] != t[i]:
                    if t[i] + s[i:] == t[i:]:
                        return True
                    else:
                        return False

            return True if len(t) - len(s) == 1 else False
