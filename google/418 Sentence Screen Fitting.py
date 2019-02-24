class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        s = ''
        for sen in sentence:
            s += sen
            s += ' '

        count = 0
        n = len(s)
        for row in range(rows):
            count += cols
            if s[count % n] == ' ':
                count += 1
            else:
                while count > 0 and s[(count - 1) % n] != ' ':
                    count -= 1

        return count // n 

        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        
