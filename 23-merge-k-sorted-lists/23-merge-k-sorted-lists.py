# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge2lists(list1, list2):
            current1, current2 = list1, list2
            sorted_current = dummy = ListNode()
            while current1 and current2:
                if current1.val <= current2.val:
                    sorted_current.next = current1
                    current1 = current1.next
                else:
                    sorted_current.next = current2
                    current2 = current2.next
                sorted_current = sorted_current.next
            if current1:
                sorted_current.next = current1
            elif current2:
                sorted_current.next = current2
            
            return dummy.next
        
        sorted_linked_list = None
        for list_ in lists:
            # print("list:", list_)
            sorted_linked_list = merge2lists(sorted_linked_list, list_)
            # print(sorted_linked_list)
        
        return sorted_linked_list