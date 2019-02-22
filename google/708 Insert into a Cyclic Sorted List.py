class Solution(object):
    def insert(self, head, insertVal):
        
        if head is None:
            return Node(insertVal, None)
        
        pre = head
        cur = pre.next
        while cur != head:
            if pre.val <= insertVal and cur.val >= insertVal:
                break
            if (pre.val > cur.val and (pre.val <= insertVal or cur.val >= insertVal)):
                break
            pre = cur
            cur = cur.next
            
        pre.next = Node(insertVal, cur)
        return head
        
