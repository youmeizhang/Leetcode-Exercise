class Solution(object):
    def numUniqueEmails(self, emails):
        n = len(emails)
        count = 0
        res = []
        for email in emails:
            email_copy = email.split("@")
            tmp = email_copy[0].replace(".", "")
            idx = tmp.index("+")
            tmp2 = tmp[:idx]
            res.append(tmp2 + email_copy[1])
        return len(list(set(res)))
