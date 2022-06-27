"""
Edge Cases:
All the linked lists provided are sorted
1. lists is empty, len(lists) == 0; return None
2. len(lists) is odd, while using conquer strategy with 2 linked lists, we will have to handle the case where there can be only 1-linked list
3. len(lists) is even

Approaches:
1. Brute Force, Use DFS
Intuition:
Keep a sorted_linked_list as None and keep merging it with every other linked list present in the lists list/array. We will have to iterate over the whole linked lists multiple times, here, k times.
Time: O(n x k) => O(n ^ 2)
Space: O(len(sorted_linked_list))

2. Use DFS with mergesort, divide and conquer strategy
Intuition:
Divide the whole lists into pairs of two linked lists, then, merge them. In the first iteration of merging we will have halved the lists array and can proceed in the same manner -> O(logk).
Time: O(nlogk)
Space: O(len(lists)) => extra space merged_lists containing the merged lists or conquered ones at a time.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # use merge sort
        if not lists:
            return None
        # keep merging until we get single sorted linked list
        while len(lists) > 1:
            # stores sorted O(logk) lists
            merged_lists = []
            # dividing the lists into pairs(group of two linked lists)
            for index in range(0, len(lists), 2):
                l1 = lists[index]
                # handle edge case for odd lengthed lists
                l2 = lists[index + 1] if index + 1 < len(lists) else None
                merged_lists.append(self.merge_lists(l1, l2))
            
            # update lists with merged_lists
            lists = merged_lists
        
        return lists[0]
    
    def merge_lists(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        dummy = tail = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        
        return dummy.next