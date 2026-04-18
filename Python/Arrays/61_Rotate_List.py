from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length and tail
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Make it circular
        tail.next = head