class Solution:
    def reorder(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        # 1. find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. reverse the second half of the linked list
        second = slow.next
        slow.next = prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # 3. merge the two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2