"""
Edge Cases:
1. nums is an empty list; return nums
2. nums has single element; return nums
3. len(nums) >= 2; find k most frequent elements and return the answer list
    3.1 nums contain multiple k most frequent elements, not possible due to constraint saying the answer is guaranteed to be unique
    3.2 nums contain unique k most frequent elements, return them

Test Cases:
1. nums = [], k = 0; return []
2. nums = [1], k = 1; return [1]
3.2 nums = [1, 1, 1, 2, 2, 3], k = 2; return [1, 2]

Approaches:
1. Brute Force
Intuition: Iterate outer for loop k times and inner for loop n times to find the element that is most frequent and unique/not considered in any of the previous iterations
Time: O(nk)
Space: O(n) storing elements of nums with its frequency

2. Use Heap
Intuition: The line top K frequent elements suggest we can use heap here as it can give us max or min elements of heap in O(logn) time. We need to store elements of nums with its frequency in a dictionary and then, build a heap of size k based on frequency and keys of the dict as elements. Later, we can return this heap as the answer.
Time: O(nlogk), O(n) to iterate over nums and build heap, O(logk) for popping out any element that is of lesser frequency than the one we encounter during iteration
Space: O(n + k), O(n) for unique elements of nums and O(k) for heap

3. Use Quick Select/Hoare's Selection Algorithm
Intuition: Select a random partition key, sort the values of nums.keys() based on this partition key(frequency). If the partition key index < k => we need to add more elements so will use partition algorithm on the right side of nums.keys() else when partition index > k, go left and when partition index == k, return the answer until k
Time: O(n), worst case O(n^2) rarely encountered due to randomization quick select
Space: O(n), for storing key value pairs of num and frequency
"""

class Solution:
    
    def __init__(self):
        self.nums = []
        self.nums_frequency_dict = {}
        self.k = 0
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        # Approach2 : Using Heap
        # stores num and its respective frequency
        nums = collections.Counter(nums)
        heap = [] # will be of size k
        for num, frequency in nums.items():
            heapq.heappush(heap, (frequency, num))
            # maintaining the size of heap to be k
            if len(heap) > k:
                heapq.heappop(heap)
        
        for index, heap_element in enumerate(heap):
            heap[index] = heap_element[1]
        
        return heap
        """        
        # Approach3 : Using Hoare's Selection/Quick Select
        self.nums_frequency_dict = collections.Counter(nums)
        self.nums = list(set(nums))
        self.k = len(self.nums)-k
        return self.quick_select(0, len(self.nums)-1)
        # print(self.nums)
        # return self.nums[self.k:]
        
    def quick_select(self, start: int, end: int) -> List[int]:
        if start > end:
            return
        partition_key_index = self.partition(start, end)
        if partition_key_index < self.k:
            return self.quick_select(partition_key_index+1, end)
        elif partition_key_index > self.k:
            return self.quick_select(start, partition_key_index-1)
        else:
            return self.nums[self.k:]
    
    def partition(self, start: int, end: int) -> int:
        random_index = random.randint(start, end)
        self.nums[random_index], self.nums[end] = self.nums[end], self.nums[random_index]
        pivot = self.nums_frequency_dict[self.nums[end]]
        pivot_index = start
        while start < end:
            if self.nums_frequency_dict[self.nums[start]] <= pivot:
                self.nums[start], self.nums[pivot_index] = self.nums[pivot_index], self.nums[start]
                pivot_index += 1
            start += 1
            
        
        self.nums[pivot_index], self.nums[end] = self.nums[end], self.nums[pivot_index]
        return pivot_index