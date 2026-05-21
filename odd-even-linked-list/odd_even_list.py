from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odd = head
        # Anchor evenHead so we can splice the even chain onto the odd chain later.
        even = evenHead = head.next

        # Weave: advance odd through odd-indexed nodes, even through even-indexed
        # nodes in tandem. Both pointers skip one node at a time within their chain.
        while odd.next and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        # Attach the full even chain to the tail of the odd chain.
        odd.next = evenHead
        return head


def build(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

sol = Solution()
print(to_list(sol.oddEvenList(build([1, 2, 3, 4, 5]))))  # [1, 3, 5, 2, 4]
print(to_list(sol.oddEvenList(build([2, 1, 3, 5, 6, 4, 7]))))  # [2, 3, 6, 7, 1, 5, 4]
