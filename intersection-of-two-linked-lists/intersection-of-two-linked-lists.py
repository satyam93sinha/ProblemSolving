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
        if not headA or not headB:
            return None
        
        currA = headA
        currB = headB
        # swap nodes when any of them reaches None
        while currA != currB:
            currA = headB if not currA else currA.next
            currB = headA if not currB else currB.next
        
        return currA