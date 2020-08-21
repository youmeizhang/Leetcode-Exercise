# credit to: https://leetcode.com/problems/reorder-list/discuss/801883/Python-3-steps-to-success-explained

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return []
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        slow.next = None
        
        head1, head2 = head, prev
        while head2:
            tmp = head1.next
            head1.next = head2
            head1 = head2
            head2 = tmp
      
        
