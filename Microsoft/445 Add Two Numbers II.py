# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        def reverse(l1):
            prev = None
            curr = l1

            while curr:
                ne = curr.next
                curr.next = prev
                prev = curr
                curr = ne

            return prev
    
        rl1 = reverse(l1)
        rl2 = reverse(l2)
        
        head = ListNode(None)
        dummy = head
        carry = 0
        
        while rl1 and rl2:
            value = rl1.val + rl2.val + carry
            temp = value % 10
            carry = value // 10
            head.next = ListNode(temp)
            head = head.next
            rl1 = rl1.next
            rl2 = rl2.next
            
        while rl1:
            value = rl1.val + carry
            temp = value % 10
            carry = value // 10
            head.next = ListNode(temp)
            head = head.next
            rl1 = rl1.next
            
        while rl2:
            value = rl2.val + carry
            temp = value % 10
            carry = value // 10
            head.next = ListNode(temp)
            head = head.next
            rl2 = rl2.next
            
        if carry:
            head.next = ListNode(carry)
            head = head.next
            
        res = reverse(dummy.next)
        return res
            
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
