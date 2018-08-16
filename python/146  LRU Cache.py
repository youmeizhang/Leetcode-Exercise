class Node:
    def __init__(self, k, x):
        self.key = k
        self.val = x
        self.next = None
        self.pre = None
        
class DoubleLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        
    def isEmpty(self):
        return not self.tail
    
    def removeLast(self):
        self.remove(self.tail)
        
    def remove(self, node):
        if self.head == self.tail:
            self.head, self.tail = None, None
            return
        if node == self.head:
            node.next.pre = None
            self.head = node.next
            return
        if node == self.tail:
            node.pre.next = None
            self.tail = node.pre
            return
        node.pre.next = node.next
        node.next.pre = node.pre
        
    def addFirst(self, node):
        if not self.head:
            self.head = self.tail = node
            node.pre = node.next = None
            return
        node.next = self.head
        self.head.pre = node
        self.head = node
        node.pre = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.p = dict()
        self.cache = DoubleLinkedList()
        
    def get(self, key):
        if (key in self.p) and self.p[key]:
            self.cache.remove(self.p[key])
            self.cache.addFirst(self.p[key])
            return self.p[key].val
        else:
            return -1
        
    def put(self, key, value):
        if key in self.p:
            self.cache.remove(self.p[key])
            self.cache.addFirst(self.p[key])
            self.p[key].val = value
        else:
            node = Node(key,value)
            self.p[key] = node
            self.cache.addFirst(node)
            self.size += 1
            if self.size > self.capacity:
                del self.p[self.cache.tail.key]
                self.size -= 1
                self.cache.removeLast()            
        
