# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = hare = head
        prev_node = None
        while hare and hare.next:
            prev_node = tortoise
            tortoise = tortoise.next
            hare = hare.next.next
        if prev_node:
            prev_node.next = tortoise.next
            return head