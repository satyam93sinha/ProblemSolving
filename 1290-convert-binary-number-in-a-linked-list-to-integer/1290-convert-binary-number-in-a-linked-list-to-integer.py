# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        length -= 1
        current = head
        result = 0
        while current:
            result += pow(2, length) * current.val
            current = current.next
            length -= 1
        
        return result