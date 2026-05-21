from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        current = head
        while current:
            n += 1
            current = current.next

        # base: minimum nodes every part receives.
        # rem: how many parts get one extra node (the leading parts).
        # Guard n > k: when n < k, base=0 and without the guard rem would
        # cause multiple nodes to land in the same part instead of one each.
        base = n // k
        rem = n % k if n > k else 0

        res = []
        next_head = head

        for i in range(k):
            if not next_head:
                res.append(None)
                continue

            section_head = current = next_head

            # Advance base-1 steps (current already sits on the first node,
            # so base-1 more moves land on the last node of this part).
            for _ in range(base - 1):
                if current.next:
                    current = current.next

            # First rem parts absorb one extra node.
            if rem > 0:
                if current.next:
                    current = current.next
                rem -= 1

            # Sever this part from the rest of the list before moving on.
            next_head = current.next
            current.next = None
            res.append(section_head)

        return res


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
parts = sol.splitListToParts(build([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)
print([to_list(p) for p in parts])  # [[1,2,3,4], [5,6,7], [8,9,10]]

parts = sol.splitListToParts(build([1, 2, 3]), 5)
print([to_list(p) for p in parts])  # [[1], [2], [3], [], []]
