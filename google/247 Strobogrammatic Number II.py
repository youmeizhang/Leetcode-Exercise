class Solution(object):
    def findStrobogrammatic(self, n):
        def helper(m, n):
            if m == 0:
                return []
            if m == 1:
                return ["0", "1", "8"]
            t = helper(m-2, n)

            res = []
            if not t:
                res.append("11")
                res.append("69")
                res.append("88")
                res.append("96")
                if m != n:
                    res.append("00")

            for a in t:    
                res.append("1" + a + "1")
                res.append("6" + a + "9")
                res.append("9" + a + "6")
                res.append("8" + a + "8")
                if m != n:
                    res.append("0" + a + "0")

            return res

        return helper(n, n)
        
        """
        :type n: int
        :rtype: List[str]
        """
        
