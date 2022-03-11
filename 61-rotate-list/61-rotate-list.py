"""
Edge Cases:
1. Head is None; return None
2. Only Head is present; return head
3. Length of linked list is greater than 1; rotate by k and return head
4. k > length of linked list; do k % length of linked list
5. k < length of linked list; do normal rotation and return head
6. k == length of linked list; anyways we are doing k % length of linked list; gives k = 0 rotation

Test Cases:
1. []
2. [3]
3. [1, 2, 3], k = 2; [2, 3, 1]
4. [1, 2, 3], k = 5; k %= length_of_linkedlist = 2; [2, 3, 1]
5. [1, 2, 3, 4], k = 4; k %= length_of_linkedlist = 0; [1, 2, 3, 4]

Approaches:
1. Brute Force
Intuition:
Find length then, do a k %= length_of_linkedlist. Traverse to length-k elements in linked list and start building a new rotated linked list with first elements as last k elements from linked list. Thereafter, reiterate over the same linked list until length-k elements and complete the rotated linked list.
Time: O(n) though we are iterating the linked list 1. calculating length, 2. end elements, 3. first length-k elements, we actually have O(3*n) ~ O(n)
Space: O(n)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge case of head is None
        if not head or not head.next:
            return head
        
        # Get the length of linked list
        length = 0
        prev, current = None, head
        # calculate length of linked list
        while current:
            length += 1
            prev = current
            current = current.next
        
        # get k <= length
        k %= length
        print(length, k)
        if k == 0:
            return head
        else:
            # point to head, circular linked list
            prev.next = head
            # remove length-k th node's next to None
            prev = prev.next  # which is head here
            current_length = 0
            while current_length != length-k-1:
                prev = prev.next
                current_length += 1
            # reached the node where rotation should have happened
            # so make it new head
            head = prev.next
            # break the connection of prev and new head, breaking the cycle
            prev.next = None
            return head
            