'''
Edge Cases:
1. len(l1) == len(l2); add the elements
2. len(l1) < or > len(l2); add the elements
3. if carry -> add this node to the end of linkedlist
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = linked_list_sum = ListNode()
        carry = 0
        while l1 or l2:
            current_sum = carry
            if l1:
                current_sum += l1.val
                l1 = l1.next
            if l2:
                current_sum += l2.val
                l2 = l2.next
            linked_list_sum.next = ListNode(current_sum%10)
            linked_list_sum = linked_list_sum.next
            carry = current_sum // 10
        
        if carry:
            linked_list_sum.next = ListNode(carry)
        
        return dummy.next