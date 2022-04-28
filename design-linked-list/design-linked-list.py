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
        self.tail = None
        self.size = -1

    def get(self, index: int) -> int:
        if index > self.size:
            return -1
        elif index == 0: # return head's value
            return self.head.val
        elif index == self.size: # return tail's value
            return self.tail.val
        else: # traverse and find the node -> return node.val
            current = self.head
            while index != 0:
                current = current.next
                index -= 1
            return current.val

    def addAtHead(self, val: int) -> None:
        if not self.head: # LinkedList is empty
            self.head = self.tail = LinkedListNode(val)
        else: # LinkedList has at least one node
            self.head = LinkedListNode(val, self.head)
        # increment size/length of linkedlist
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        if not self.tail:  # LinkedList is empty
            return self.addAtHead(val)
        else:  # LinkedList is not empty
            self.tail.next = LinkedListNode(val)
            self.tail = self.tail.next
            self.size += 1
            

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:  # add at head
            return self.addAtHead(val)
        elif index == self.size+1:  # index is length of linked list, length is always 1-indexed
            return self.addAtTail(val)
        elif index > self.size+1:  # invalid case
            return
        else:  # 1 < index < length of linked list
            prev, current = None, self.head
            while index != 0:
                prev = current
                current = current.next
                index -= 1
            prev.next = LinkedListNode(val, current)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:  # remove from head
            self.head = self.head.next
        elif index > self.size:  # index is invalid
            return
        else:  # 0 < index <= size of index
            prev, current = None, self.head
            current_index = 0
            while current_index != index:
                prev = current
                current = current.next
                current_index += 1
            prev.next = current.next
            if not prev.next:
                self.tail = prev
        # decrement length/size of linked list
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)