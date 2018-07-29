# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        fast = slow = head
        while (fast != None):
            if fast.next != None:
                fast = fast.next.next
                slow = slow.next
            else:
                break
        return slow
