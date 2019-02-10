from queue import *
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        self.buffer = Queue()
        self.end = False
        if n == 0:
            return 0
        count = 0
        while self.buffer.qsize() < n and not self.end:
            buf4 = [""] * 4
            tmp = read4(buf4)
            if tmp < 4:
                self.end = True
            for i in range(tmp):
                self.buffer.put(buf4[i])
        for i in range(min(self.buffer.qsize(), n)):
            buf[i] = self.buffer.get()
            count += 1
        return count
