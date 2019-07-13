# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        
        cnt = 0
        cur = head
        while cur and cnt != k:
            cur = cur.next
            cnt += 1
        if cnt == k:
            cur = self.reverseKGroup(cur, k)
            while cnt > 0:
                temp = head.next
                head.next = cur
                cur = head
                head = temp
                cnt -= 1
            head = cur
        return head
                
