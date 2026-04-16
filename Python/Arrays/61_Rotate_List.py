from typing import Optional,List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head

        length,tail=1,head
        while tail.next:
            tail=tail.next
            length+=1

        tail.next=head

        steps=length-(k%length)
        for  _  in range(steps):
            tail=tail.next

        
        new_head=tail.next
        tail.next=None
        return new_head
        