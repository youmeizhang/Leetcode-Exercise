class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.n = len(compressedString)
        self.cnt = 0

        self.char = compressedString[0]

        self.string = compressedString
        
        for i in range(self.n):
            if compressedString[i].isdigit():
                j = i
                while j < self.n and compressedString[j].isdigit():
                    j += 1
                self.cnt = int(compressedString[i:j])
                self.start = j

                break

    def next(self):
        """
        :rtype: str
        """
        if self.cnt > 0:
            self.cnt -= 1
            return self.char
        
        elif self.cnt == 0 and self.start < self.n:
            self.start += 1
            self.char = self.string[self.start-1]
            begin = self.start
            
            while self.start < self.n and self.string[self.start].isdigit():
                self.start += 1

            self.cnt = int(self.string[begin:self.start])
    
            self.cnt -= 1
            return self.char
        else:
            return ' '
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cnt > 0:
            return True
        if self.start < self.n:
            return True
        return False
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.queue = []
        for token in re.findall('\D\d+', compressedString):
            self.queue.append((token[0], int(token[1:])))
        self.cnt = 0
        self.char = ''

    def next(self):
        """
        :rtype: str
        """
       
        if self.cnt > 0:
            self.cnt -= 1
            return self.char
        elif self.cnt == 0 and self.queue:
            token = self.queue.pop(0)
            self.char, self.cnt = token[0], token[1]
            self.cnt -= 1
            return self.char
        else:
            return ' '
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cnt > 0:
            return True
        elif self.cnt == 0 and self.queue:
            return True
        return False
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
