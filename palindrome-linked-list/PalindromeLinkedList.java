public class PalindromeLinkedList {

    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null)
            return true;
        
        // find the middle node
        ListNode slow = head, fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // reverse the second half
        ListNode current = slow;
        ListNode previous = new ListNode();
        while (current != null) {
            ListNode next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }

        //compare both halves
        ListNode left = head;
        ListNode right = previous;
        while (right != null) {
            if (right.val != left.val)
                return false;
            left = left.next;
            right = right.next;
        }
        return true;
    }
}

class ListNode {
    int val;
    ListNode next;

    ListNode() {}

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}