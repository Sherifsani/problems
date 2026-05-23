/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
public class MaxTwinSum {
    public int pairSum(ListNode head) {
        // fast starts at head.next (not head) so that when fast reaches the
        // last node, slow lands at the last node of the first half.
        ListNode slow = head, fast = head.next;
        while (fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        // Reverse the second half in-place. After this loop, prev is the
        // original last node and is now the head of the reversed second half.
        ListNode prev = slow;
        ListNode current = slow.next;
        while (current != null) {
            ListNode next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        // Re-link: slow (end of first half) → prev (head of reversed second half).
        // This lets the traversal below walk both halves with a single pointer each.
        slow.next = prev;

        int sum = 0;
        current = head;
        slow = slow.next;   // slow now points to the reversed second half's head
        // Stop when the left pointer reaches prev (the original last node).
        // For a list of length n the loop runs exactly n/2 times, covering all pairs.
        while (!current.equals(prev)) {
            sum = (int) Math.max(sum, current.val + slow.val);
            current = current.next;
            slow = slow.next;
        }

        return sum;
    }
}
