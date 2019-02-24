# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        self.flag = False
        self.prev = None
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        

    def peek(self):
        if not self.flag:
            self.prev = self.iter.next()
            self.flag = True

        return self.prev
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        

    def next(self):
        if self.flag:
            prev = self.prev
            self.prev = None
            
            self.flag = False
            return prev
        else:
            return self.iter.next()
        """
        :rtype: int
        """
        

    def hasNext(self):

        return self.iter.hasNext() or self.flag
        """
        :rtype: bool
        """
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
