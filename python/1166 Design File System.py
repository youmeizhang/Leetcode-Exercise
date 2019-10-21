class FileSystem(object):

    def __init__(self):
        self.dic = {"": -1, "/": -1}
        

    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        parent = path[:path.rfind('/')]
        
        if path not in self.dic and parent in self.dic:
            self.dic[path] = value
            return True
        return False
    
        

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        if path in self.dic:
            return self.dic[path]
        return -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
