class Solution(object):
    def toHex(self, num):
        if num < 0:
            num += 0x100000000
        ref = '0123456789abcdef'
        ans = []
        while(num):
            ans.append(ref[int(num % 16)])
            num = num // 16
        return ''.join(ans[::-1]) if ans else '0'
