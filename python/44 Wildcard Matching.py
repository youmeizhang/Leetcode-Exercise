class Solution(object):
    def isMatch(self, s, p):
        if not p:
            return not s
        sp = pp = match = 0
        start = -1
        while (sp < len(s)):
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == "?"):
                sp += 1
                pp += 1
            elif pp < len(p) and p[pp] == "*":
                start = pp
                match = sp
                pp += 1
            elif start != -1:
                pp = start + 1
                match += 1
                sp = match
            else:
                return False
        while (pp < len(p) and p[pp] == "*"):
            pp += 1
        return pp == len(p)
