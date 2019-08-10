# credit to: http://bookshadow.com/weblog/2017/05/21/leetcode-design-in-memory-file-system/

class FileSystem(object):

    def __init__(self):
        self.root = {'dir' : {}, 'file': {}}
    
    def getNode(self, path):
        node = self.root
        for dir in filter(len, path.split('/')):
            if dir in node['dir']:
                node = node['dir'][dir]
            else:
                return node, 'file'
        return node, 'dir'

    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        #print(self.root)
        node, type = self.getNode(path)
        if type == 'dir':
            return sorted(node['dir'].keys() + node['file'].keys())
        return [path.split('/')[-1]]            

    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        node = self.root
        for dir in filter(len, path.split('/')):

            if dir not in node['dir']:
                node['dir'][dir] = {'dir': {}, 'file': {}}
                        
            node = node['dir'][dir]
                    
    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        dir = filePath.split('/')
        path, file = '/'.join(dir[:-1]), dir[-1]
        self.mkdir(path)
        node, type = self.getNode(path)
        if file not in node['file']:
            node['file'][file] = ''

        node['file'][file] += content

    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        dir = filePath.split('/')
        path, file = '/'.join(dir[:-1]), dir[-1] 
        node, type = self.getNode(path)
        return node['file'][file]
        
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
