class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;
        ListNode fast = head;
        ListNode slow = head;
        
        while(fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        
        ListNode second = slow.next;
        
        ListNode p1 = second;
        ListNode p2 = p1.next;
        
        slow.next = null;
        
        while(p1 != null && p2 != null) {
            ListNode t = p2.next;
            p2.next = p1;
            p1 = p2;
            p2 = t;
        }
        
        while(p1 != null) {
            if (head.val != p1.val) return false;
            head = head.next;
            p1 = p1.next;
        }
        return true;
    }
}
