# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Edge Cases:
    1. headA is None, headB is not None --> no intersection
    2. headA and headB are not None, no intersection
    3. headA is short, headB is long --> intersection present
    4. headA is long, headB is short --> intersection present
    5. headA and headB are None, no intersection
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # find length of both the Linked Lists
        lengthA, lengthB = self.getLength(headA), self.getLength(headB)
        # iterate the longer LL until both are of the same length, do not modify headA or headB
        currA, currB = headA, headB
        if lengthA > lengthB:
            currA = self.moveHead(headA, lengthA-lengthB)
        elif lengthB > lengthA:
            currB = self.moveHead(headB, lengthB-lengthA)
        
        while currA and currB and currA != currB:
            currA = currA.next
            currB = currB.next
        
        if currA == currB:
            return currA
            
        
    def getLength(self, head: ListNode) -> int:
        length = 0
        while head:
            head = head.next
            length += 1
        return length
    
    def moveHead(self, head: ListNode, move: int) -> Optional[ListNode]:
        while head and move:
            head = head.next
            move -= 1
        return head