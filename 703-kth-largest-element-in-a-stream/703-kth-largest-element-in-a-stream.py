"""
Edge Cases:
1. nums is empty; so no kth largest element can be found
2. len(nums) == 1; we can have only one kth largest element provided k<=len(nums); return nums[0]
3. len(nums) >= 2; find kth largest element and return that integer value
    3.1 the stream happens only once, return kth largest element directly
    3.2 stream of adding values to nums list, the kth largest element gets changed due to addition of new values to nums or keeps changing
    3.2 the addition of values in stream do not change kth largest element found in the first place
    
Test Cases:
1. [], k = 0
2. [1], k = 1 ; return 1
3.1 [1, 2], k = 1; return 2
3.2 [1, 2], add -> 5, 4, 6, 8, k = 2; return 6
3.3 [8, 6], add -> 5, 4, 1, 2, k = 2; return 6

Approaches:
1. Brute Force
Intuition: Keep the nums list sorted and sort whenever a new element is added returning the kth-largest element using the index of nums.
Time: O(n^2 logn), O(n) for stream and O(nlogn) for sorting the nums list
Space: O(n) considering we have nums list

2. Use Heap
Intuition: Maxheapify the nums list and everytime a new element is added, it will be added at its correct place in maxheap in O(logn) time. We need to pop k-elements to get kth largest element if we don't use nlargest function/inbuilt method of heapq.
Time: O(nlogn), O(n) for stream and building heap(only once), O(logn) to add, pop an element from heap
Space: O(n) considering we have nums list

3. Use Heap of size k
Intuition: Store only k elements in heap minheapifying them. 
Why minheapify?
Ans: so that we have first element of heap as kth largest element
Time: O(nlogk), O(n) for data stream and O(logk) to add new values to nums/heap
Space: O(k) we will be storing only required k elements
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            if len(self.heap) < k:
                heapq.heappush(self.heap, num)
            elif len(self.heap) == k and self.heap[0] < num:
                heapq.heapreplace(self.heap, num)
        # print("Heap initialised:", self.heap)

    def add(self, val: int) -> int:
        # heap is already of size k
        # so we need to pop the smallest element and push new one
        # iff smallest element is smaller than current val
        if self.heap and self.heap[0] < val and len(self.heap) == self.k:
            heapq.heapreplace(self.heap, val)
        elif len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)