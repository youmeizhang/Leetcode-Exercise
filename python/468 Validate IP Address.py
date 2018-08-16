class Solution:
    def validIPAddress(self, IP):
        IP4 = any(i in '.' for i in IP)
        IP6 = any(i in ':' for i in IP)

        if IP4:
            l4 = IP.split(".")
            if len(l4) != 4:
                return "Neither"
            for i in l4:
                if not i.isdigit():
                    return "Neither"
                elif int(i) < 256 and int(i) > -1:
                    if i.startswith("0") and len(i) > 1: 
                        return "Neither"
                else:
                    return "Neither"
            return "IPv4"

        elif IP6:
            l6 = IP.split(":")
            if len(l6) != 8:
                return "Neither"
            for i in range(8): 
                if l6[i] == '':
                    return "Neither"
                elif len(l6[i]) > 4:
                    return "Neither"  
                elif not all(c in string.hexdigits for c in l6[i]):
                    return "Neither"

            return "IPv6"

        else:
            return "Neither"
