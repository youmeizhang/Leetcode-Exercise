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
        
# credit to: https://blog.csdn.net/fuxuemingzhu/article/details/79380457
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s1 = []
        s2 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
            
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = ListNode(None)
        dummy = head
        value = 0
        answer = None
        
        while s1 and s2:
            p1 = s1.pop()
            p2 = s2.pop()
            value = p1 + p2 + carry
            temp = answer
            carry = value // 10
            answer = ListNode(value % 10)
            answer.next = temp
            
        l = s1 if s1 else s2
        while l:
            value = l.pop() + carry
            temp = answer
            carry = value // 10
            answer = ListNode(value % 10)
            answer.next = temp
            
        if carry :
            temp = answer
            answer = ListNode(carry)
            answer.next = temp
            
        return answer
