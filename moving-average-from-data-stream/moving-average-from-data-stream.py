class MovingAverage:

    def __init__(self, size: int):
        self.length = size
        self.queue = collections.deque()
        self.size = 0
        self.current_sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.current_sum += val
        self.size += 1
        
        if self.size > self.length:
            self.current_sum -= self.queue.popleft()
            self.size -= 1
        
        return self.current_sum / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)