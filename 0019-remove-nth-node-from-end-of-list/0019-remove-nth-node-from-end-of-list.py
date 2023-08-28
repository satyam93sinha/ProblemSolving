# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            current = current.next
            length += 1
        
        length = length - n - 1
        if length < 0:
            return head.next
        
        current = head
        while length:
            current = current.next
            length -= 1
        current.next = current.next.next
        return head