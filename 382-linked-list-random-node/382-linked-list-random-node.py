# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = current = head
        self.size = 0
        self.position_node = {}
        while current:
            self.size += 1
            self.position_node[self.size] = current.val
            current = current.next
        
    def getRandom(self) -> int:
        index = random.randint(1, self.size)
        return self.position_node[index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()