class Solution(object):
    def gcdOfStrings(self, str1, str2):

        def gcd(str1, str2):
            if len(str1) > len(str2):
                for i in range(len(str2)):
                    if str1[i] != str2[i]:
                        return ''
                return gcd(str1[len(str2):], str2)
            elif len(str1) < len(str2):
                return gcd(str2, str1)
            else:
                if str1 == str2:
                    return str1
                else:
                    return ''
                
        return gcd(str1, str2)
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
