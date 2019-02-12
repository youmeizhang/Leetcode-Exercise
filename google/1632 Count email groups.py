class Solution:
    """
    @param emails: Original email
    @return: Return the count of groups which has more than one email address in it.
    """
    def countGroups(self, emails):
        # Write your code here
        dic = collections.defaultdict(int)
        for email in emails:
            email = email.split("@")
            former = email[0].replace(".", "")
            latter = email[1]
            
            pidx = former.find("+")
            if pidx == -1:
                dic[former + latter] += 1
                
            else:
                dic[former[:pidx] + latter] += 1
        count = 0
        for i, key in enumerate(dic):
            #print(key, dic[key])
            
            if dic[key] > 1:
                count += 1
        return count
