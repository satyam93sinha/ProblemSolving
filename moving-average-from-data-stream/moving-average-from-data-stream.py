'''
Edge Cases:
1. MovingAverage size (window size = 1), return whatever is input
2. MovingAverageSize (window size = 0), not possible, a constraint
3. MovingAverageSize (window size > 1), calculate running avg and return answer
4. MovingAverageSize (window size >= 1), array is nothing, what to return?

Test Cases:
["MovingAverage", "next", "next"]
[[1], [1], [2]]

["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]

["MovingAverage"]
[[1]]

Approaches:
Brute Force
Intuition:
Maintain a queue of length = window size, every time calculate sum O(n) worst case time complexity then calculate average
Time: as max calls made will be 104, thus, 104O(n) ==> O(n) time complexity
Space: O(window size) --> O(n) in worst case for maintaining queue

Optimised
Intuition:
In addition to the brute force queue, maintain a sum that calculates sum of values as we slide the window and when window size is reached, we can popleft queue's front value and subtract from sum, calculate average and return
Time: O(1), it can be max O(104) as these many calls are made to next and the average calculation stays O(1)
Space: O(window size or n) for maintaining queue
'''

class MovingAverage:

    def __init__(self, size: int):
        self.window_size = size
        self.current_sum = 0
        self.queue = collections.deque()

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.current_sum += val
        current_size = len(self.queue)
        
        if current_size > self.window_size:
            self.current_sum -= self.queue.popleft()
            current_size -= 1
        
        return self.current_sum / current_size
            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)