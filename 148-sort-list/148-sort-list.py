# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(nlogn), Space: O(logn), which is height of a binary tree
        return self.divide(head)
        
    def linked_list_mid(self, head):
        tortoise, hare = head, head
        prev = None
        
        while hare and hare.next:
            prev = tortoise
            tortoise = tortoise.next
            hare = hare.next.next
        
        prev.next = None
        return tortoise
    
    def divide(self, head):
        if not head or not head.next:
            return head
        
        mid = self.linked_list_mid(head)
        left = self.divide(head)
        right = self.divide(mid)
        return self.merge(left, right, head)
    
    def merge(self, left, right, head):
        dummy = current = ListNode(next = head)
        
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        
        while left:
            current.next = left
            left = left.next
            current = current.next
        
        while right:
            current.next = right
            right = right.next
            current = current.next
        
        return dummy.next
    