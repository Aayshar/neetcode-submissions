# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None

        prev=None
        current=second

        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node

        second=prev
        first=head
        while second:
            next_first=first.next
            next_second=second.next

            first.next=second
            second.next=next_first

            first=next_first
            second=next_second



        