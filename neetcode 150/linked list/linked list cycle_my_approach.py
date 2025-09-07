# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hSet = set()
        prev, curr = None, head

        while curr:
            if curr.next in hSet:
                return True
            hSet.add(curr)
            curr = curr.next
        return False