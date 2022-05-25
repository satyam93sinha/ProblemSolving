class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [0 for _ in range(k)]
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front = self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
            
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.front == self.rear:  # single element, remove pointers/indices
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        return -1
        

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.rear]
        return -1
        

    def isEmpty(self) -> bool:
        if self.front == -1:
            return True
        return False

    def isFull(self) -> bool:
        if (self.rear + 1) % self.size == self.front:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()