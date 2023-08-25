# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        match_node = self.has_cycle(head)
        # if not cycle: return match_node
        curr_node = head
        while curr_node and match_node and curr_node != match_node:
            curr_node = curr_node.next
            match_node = match_node.next
        return match_node
    
    def has_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = hare = head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if tortoise == hare: return hare
        
        return None