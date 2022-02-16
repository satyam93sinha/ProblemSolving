"""
Edge Cases:
1. head is empty -> return head
2. single element -> return head
3. Even length of linked list
4. Odd length of linked list
                            prev
    1 <- 2 <- 3 <- 4 <- 5 <- 6
                                curr nxt
None <- 1 <- 2 <- 3 <- 4 <- 5
prev
None <- 1 None
    curr    nxt
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev