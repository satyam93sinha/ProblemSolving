# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # binary representation
        # notice: 110 
        # 1*2 + 1 => 3
        # 3*2 + 0 => 6 loop breaks
        # 6*2 + 0 => 12 loop breaks
        num = head.val  # head is non-empty
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num
        
        """
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
        """