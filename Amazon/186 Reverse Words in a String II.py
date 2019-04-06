class Solution(object):
    def reverseWords(self, s):
        s.reverse()
        n = len(s)
        tmp = []
        start = 0
        end = 0

        for i in range(n):
            if s[i] != " ":
                tmp.append(s[i])
            else:
                end = i
                k = 0
                m = len(tmp)
                for j in range(start, end):
                    s[j] = tmp[m - k - 1]
                    k += 1
                tmp = []
                start = i + 1

        k = 0
        m = len(tmp)
        for j in range(start, n):
            s[j] = tmp[m - k - 1]
            k += 1
      
        """
        :type str: List[str]
        :rtype: None Do not return anything, modify str in-place instead.
        """
        
