"""
Edge Cases:
1. head is None, No head; return head/None
2. only head is present; we do nothing; return head
3. even length of linked list, we reverse every pair; return new head
4. odd length of linked list, we reverse pairs and then leave the last one; return new head

Test Cases:
a) dummy -> 1 -> 2 -> 3 -> 4
   prev   curr
                2nd   nxt

   dummy -> 2 -> 1 -> 3 -> 4
   prev     2nd curr  nxt
   
   dummy -> 2 -> 1    3 -> 4 -> None
                prev curr
                           2nd   nxt

   dummy -> 2 -> 1 -> 4 -> 3 -> None
                prev 2nd  curr   nxt

b) dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
   prev   curr
                2nd   nxt

   dummy -> 2 -> 1 -> 3 -> 4 -> 5 -> None
   prev     2nd curr  nxt
   
   dummy -> 2 -> 1    3 -> 4 -> 5 -> None
                prev curr
                           2nd  nxt

   dummy -> 2 -> 1 -> 4 -> 3 -> 5 -> None
                prev 2nd  curr  nxt
    
   dummy -> 2 -> 1 -> 4 -> 3 -> 5 -> None
                          prev  curr
Approaches:
1. Using Loop
Intuition:
As shown above in Test Cases
Time: O(n)
Space: O(1) not using any extra space
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, current = dummy, head
        
        while current and current.next:
            # track next pointers
            next_pair = current.next.next
            second_node = current.next
            
            # reverse pair
            prev.next = second_node
            second_node.next = current
            current.next = next_pair
            
            # update the pointers
            prev = current
            current = next_pair
        
        return dummy.next
            