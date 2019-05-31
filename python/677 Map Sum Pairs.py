# credit to: https://blog.csdn.net/fuxuemingzhu/article/details/79436619

class Node:
    def __init__(self, count = 0):
        self.children = collections.defaultdict(Node)
        self.count = count
    
class MapSum(object):

    def __init__(self):
        self.root = Node()
        self.keys = {}
        """
        Initialize your data structure here.
        """
        

    def insert(self, key, val):
        curr = self.root
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val
        curr = self.root
        curr.count += delta
        
        for char in key:
            curr = curr.children[char]
            curr.count += delta
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        

    def sum(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count
        """
        :type prefix: str
        :rtype: int
        """
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
