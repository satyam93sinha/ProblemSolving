# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tortoise = hare = head
        prev = None
        while hare and hare.next:
            hare = hare.next.next
            nxt = tortoise.next
            tortoise.next = prev
            prev = tortoise
            tortoise = nxt
        
        if hare:
            tortoise = tortoise.next
        
        while tortoise and prev and tortoise.val == prev.val:
            tortoise = tortoise.next
            prev = prev.next
        
        return tortoise == prev