# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        n = 0
        dummy = head
        while dummy:
            n += 1
            dummy = dummy.next
        if n == 0:
            return []
        res = [0] * n
        index = []
        pos = 0
        
        while head:
            if len(index) != 0 and index[-1][0] < head.val:
                res[index[-1][1]] = head.val
                index = index[:-1]
            else:
                index.append((head.val, pos))
                head = head.next
                pos += 1
        return res
                  
        """
        :type head: ListNode
        :rtype: List[int]
        """
        
