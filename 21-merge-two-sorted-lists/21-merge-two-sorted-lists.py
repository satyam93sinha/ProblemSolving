# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = sorted_linked_list = ListNode()
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    sorted_linked_list.next = list1
                    list1 = list1.next
                else:
                    sorted_linked_list.next = list2
                    list2 = list2.next            
            elif list1:
                sorted_linked_list.next = list1
                list1 = list1.next
            elif list2:
                sorted_linked_list.next = list2
                list2 = list2.next
            
            sorted_linked_list = sorted_linked_list.next
        
        return dummy.next