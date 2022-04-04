"""
Edge Cases:
1. Head is None; a constraint so not possible
2. Only head is present as a Node in linked list; return head
3. length(linked list) > 1
    3.1 nodes to be swapped are head and tail nodes
    3.2 nodes to be swapped are neither head nor tail nodes

Approaches:
1. Brute Force, use dummy node to not worry about handling swap of head and tail nodes and not get a None has no next exception
Intuition: We can get kth node from beginning of the linked list and its previous needed during swap. In order to get the kth node from end of the linked list we need to calculate length of linked list and then find the prev_end and k_node_end.
Once all of them are found we can swap(prev_begin.next, prev_end.next) to place k_node_begin and k_node_end at their respective places, we are not done yet, we need to change their next pointers too so swap(k_node_begin.next, k_node_end.next).
Time: O(n) We only visit every node/iterate linked list thrice, calculating length, getting node from beginning and getting node from end.
Space: O(1) no extra space used apart from the objects/variables required to keep track of nodes.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge Case-2, when head is the only node in linked list
        if not head.next:
            return head
        
        # calculate length of linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Set a dummy node
        dummy = ListNode(-1, head)

        # find the prev and k_node from beginning of the linked list
        prev_begin, k_node_begin = dummy, head
        begin = k-1
        while begin > 0 and k_node_begin:
            begin -= 1
            prev_begin = k_node_begin
            k_node_begin = k_node_begin.next
        
        # find the prev and k_node from end of the linked list
        prev_end, k_node_end = dummy, head
        end = length-k
        while end > 0 and k_node_end:
            end -= 1
            prev_end = k_node_end
            k_node_end = k_node_end.next
        
        # swap nodes
        prev_begin.next, prev_end.next = k_node_end, k_node_begin
        k_node_begin.next, k_node_end.next = k_node_end.next, k_node_begin.next
        
        return dummy.next