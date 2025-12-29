# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
       dummy = ListNode(0)
       dummy.next = head

       current = head
       previous = dummy

       while current:
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
       return dummy.next
                
'''
uses a dummy node to handle edge cases where the head node needs to be removed.
this way head removal is treated the same as any other node removal.
'''