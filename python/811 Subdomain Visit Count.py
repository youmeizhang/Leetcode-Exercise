class Solution(object):
    def subdomainVisits(self, cpdomains):
        dic = collections.defaultdict(int)
        for cpdomain in cpdomains:
            l = cpdomain.split(" ")
            count = int(l[0])
            domain = l[1]
            
            dic[domain] += count
            for i in range(len(domain)):
                if domain[i] == ".":
                    dic[domain[i+1:]] += count

        res = []
        tmp = ""
        for k in dic.keys():
            tmp += str(dic[k])
            tmp += " "
            tmp += k
            res.append(tmp)
            tmp = ""
            
        return res
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
