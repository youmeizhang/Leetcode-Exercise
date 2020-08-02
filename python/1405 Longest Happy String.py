# credit to: https://www.youtube.com/watch?v=JnhaTHSx4Xw

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        while a + b + c > 0:
            if a == max(a, b, c):
                if res[-2:] != "aa":
                    res += "a"
                    a -= 1
                elif max(b ,c) > 0:
                    if b >= c:
                        res += "b"
                        b -= 1
                    else:
                        res += "c"
                        c -= 1
                else:
                    break
                
            elif b == max(a, b, c):
                if res[-2:] != "bb":
                    res += "b"
                    b -= 1
                elif max(a ,c) > 0:
                    if a >= c:
                        res += "a"
                        a -= 1
                    else:
                        res += "c"
                        c -= 1
                else:
                    break
            elif c == max(a, b, c):
                if res[-2:] != "cc":
                    res += "c"
                    c -= 1
                elif max(b ,a) > 0:
                    if b >= a:
                        res += "b"
                        b -= 1
                    else:
                        res += "a"
                        a -= 1
                else:
                    break
        return res
                    
                
        
