# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(a: Optional[ListNode], b: Optional[ListNode], carry: int) -> Optional[ListNode]:
            if not a and not b and carry == 0:
                return None
            x = a.val if a else 0
            y = b.val if b else 0
            s = x + y + carry
            node = ListNode(s % 10)
            node.next = add(a.next if a else None, b.next if b else None, s // 10)
            return node

        return add(l1, l2, 0)
