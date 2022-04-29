"""
Edge Cases:
All nodes in the linked list are 0-indexed.
1. get()
    i) index > length of linked list so return -1; covers the case when linked list is empty
    ii) 0 <= index < length of linked list so return the value of this node
2. addAtHead() -> increment length
    i) linked list is empty; add the node and make it head; make tail to point to this node as its the only node present in linked list.
    ii) linked list is not empty; add the node and make current head as its next
3. addAtTail()
    i) linked list is empty use addAtHead() function to add the node and make it as head, increment of length will happen inside addAtHead()
    ii) linked list is not empty, add the node at tail and make the tail pointer point to this tail/update tail pointer, increment length of linked list
4. addAtIndex()
    i) index == 0; use addAtHead()
    ii) index == length of linked list; use addAtTail()
    iii) 0 < index < length of linked list; traverse to find prev node and add this node to the next of prev and increment length of linked list
5. deleteAtIndex() -> decrement length
    i) index == 0; head = head.next; length -= 1
    ii) index == length of linked list; traverse to prev of tail and delete its next pointer, update tail, length -= 1
    iii) 0 < index < length of linked list; find prev and delete its next pointer, length -= 1
    
"""
class LinkedListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

class MyLinkedList:

    def __init__(self):
        self.head = None
    
    def get_node(self, index: int) -> LinkedListNode:
        current = self.head
        while index != 0 and current:
            current = current.next
            index -= 1
        
        return current
    
    def get(self, index: int) -> int:
        node = self.get_node(index)
        return node.val if node else -1
        
    def addAtHead(self, val: int) -> None:
        node = LinkedListNode(val, self.head)
        self.head = node

    def get_tail(self) -> LinkedListNode:
        current = self.head
        while current and current.next:
            current = current.next
        
        return current
    
    def addAtTail(self, val: int) -> None:
        current_tail = self.get_tail()
        if current_tail:
            current_tail.next = LinkedListNode(val)
        else:
            self.addAtHead(val)
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)
        else:
            get_prev_node = self.get_node(index-1)
            if get_prev_node:
                get_prev_node.next = LinkedListNode(val, get_prev_node.next)
        
        
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        else:
            get_prev_node = self.get_node(index-1)
            if get_prev_node and get_prev_node.next:
                get_prev_node.next = get_prev_node.next.next

        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)