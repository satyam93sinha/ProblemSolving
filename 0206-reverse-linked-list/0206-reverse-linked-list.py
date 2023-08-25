# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        curr_node = head
        new_head = None
        while curr_node:
            new_node = ListNode(curr_node.val, new_head)
            new_head = new_node
            curr_node = curr_node.next
        
        return new_head