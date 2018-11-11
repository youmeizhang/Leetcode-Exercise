class Solution(object):
    def reorderLogFiles(self, logs):
        res = []
        digits = []
        for log in logs:
            if log.split(" ")[1].isdigit():
                digits.append(log)
            else:
                res.append(log)
                
        res.sort(key=lambda x:(x.split(" ")[1], x.split(" ")[0].isdigit()))
        return res + digits
