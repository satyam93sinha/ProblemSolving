class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_stack.append(val)
        else:
            self.stack.append(val)
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        if not self.stack:
            return
        else:
            self.stack.pop()
            self.min_stack.pop()
            '''
            if self.top() == self.min_stack[-1]:
                self.stack.pop()
                self.min_stack.pop()
            else:
                self.stack.pop()
            '''
        
    
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()