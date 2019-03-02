"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
from Queue import Queue
class Solution(object):
    def __init__(self):
        self.buffer = Queue()
        self.end = False
        
    def read(self, buf, n):
        
        
        if n == 0:
            return 0
        
        total = 0
        while self.buffer.qsize() < n and not self.end:
            bufn = [""] * 4
            tmp = read4(bufn)
            if tmp < 4:
                self.end = True
            
            for i in range(tmp):
                self.buffer.put(bufn[i])
                
        for i in range(min(self.buffer.qsize(), n)):
            buf[i] = self.buffer.get()
            total += 1
            
        return total
        
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        
