class Logger(object):

    def __init__(self):
        self.dic = {}
        """
        Initialize your data structure here.
        """
        
    def shouldPrintMessage(self, timestamp, message):
        if message not in self.dic:
            self.dic[message] = timestamp
            return True
        elif timestamp - self.dic[message] >= 10:
            self.dic[message] = timestamp
            return True
        else:
            return False
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
