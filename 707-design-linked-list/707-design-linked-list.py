"""
Edge Cases:
All the methods/functions will be 0-indexed
1. get()
    i) index is greater than the size of linked list; return -1
    ii) 0 <= index < size of linked list; return the node
2. addAtHead(val) -> increment length
    i) head is None; make the val as head
    ii) head is already present; ListNode(val) -> head;
3. addAtTail(val)
    i) head is None; add it at head
    ii) else add to the end of linked list -> increment length
4. addAtIndex(index, val)
    i) head is None, says to add at 0-index; addAtHead(val)
    ii) index == size of linked list; addAtTail(val)
    iii) 0 < index < size of linked list; add node at this index
    iv) index > size of linked list; do nothing ; increment length
5. deleteAtIndex(index)
    i) index = 0; removeFromHead() -> decrement length
    ii) 0 < index <= size of linked list - 1; remove tail
    iii) index > size of linked list; do nothing
"""
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = -1

    def getHead(self):
        return self.head.val if self.head else -1
    
    def getTail(self):
        return self.tail.val if self.tail else -1
    
    def get(self, index: int) -> int:
        if index == 0:
            return self.getHead()
        elif index == self.size:
            return self.getTail()
        elif index > self.size:
            return -1
        else:
            # 0 < index < self.size
            current = self.head
            while current and index > 0:
                current = current.next
                index -= 1
            return current.val

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = self.tail = ListNode(val)
        else:
            self.head = ListNode(val, self.head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if not self.head:
            return self.addAtHead(val)
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)
        elif index == self.size+1:
            return self.addAtTail(val)
        elif index > self.size+1:
            # invalid index
            return
        else:
            # 0 < index <= self.size
            prev, current = None, self.head
            while current and index > 0:
                prev = current
                current = current.next
                index -= 1
            prev.next = ListNode(val, current)
            self.size += 1
    
    def removeFromHead(self):
        if self.head:
            self.head = self.head.next
            self.size -= 1
        return

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            return self.removeFromHead()
        elif index > self.size:
            return
        else:
            prev, current = None, self.head
            while current and index > 0:
                prev = current
                current = current.next
                index -= 1
            prev.next = current.next
            if prev.next == None:
                self.tail = prev
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)