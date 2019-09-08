# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = first = ListNode(None)
        dummy2 = second =  ListNode(None)
        
        while head:
            if head.val < x:
                first.next = ListNode(head.val)
                head = head.next
                first = first.next
            else:
                second.next = ListNode(head.val)
                head = head.next
                second = second.next
                
        first.next = dummy2.next
        return dummy.next
        
