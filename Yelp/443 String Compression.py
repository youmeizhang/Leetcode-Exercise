class Solution(object):
    def compress(self, chars):
        n = len(chars)
        curr = chars[0]
        count = 1
        if n == 1:
            return 1
        
        pos = 0
        for i in range(1, n):
            if chars[i] == curr:
                count += 1
            else:
                if count > 1:
                    chars[pos] = curr
                    pos += 1
                    tmp = str(count)
                    for j in range(len(tmp)):
                        chars[pos] = tmp[j]
                        pos += 1
                else:
                    chars[pos] = curr
                    pos += 1
                    
                
                curr = chars[i]
                count = 1
        chars[pos] = curr
        pos += 1
        if count > 1:
            tmp = str(count)
            for j in range(len(tmp)):
                chars[pos] = tmp[j]
                pos += 1
        return pos
                
        """
        :type chars: List[str]
        :rtype: int
        """
        
