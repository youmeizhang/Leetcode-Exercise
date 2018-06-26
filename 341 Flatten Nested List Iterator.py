class NestedIterator(object):

    def __init__(self, nestedList):
        self.queue = collections.deque()
        def getAll(nests):
            for nest in nests:
                if nest.isInteger():
                    self.queue.append(nest.getInteger())
                else:
                    getAll(nest.getList())
        getAll(nestedList)
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        

    def next(self):
        return self.queue.popleft()
        """
        :rtype: int
        """
        

    def hasNext(self):
        return len(self.queue)
        """
        :rtype: bool
        """
