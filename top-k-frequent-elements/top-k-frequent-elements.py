from heapq import heappush, heappop
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_frequency = Counter(nums)
        heap = []
        for num, frequency in nums_frequency.items():
            heappush(heap, (frequency, num))
            if len(heap) > k:
                heappop(heap)
        
        for index, element in enumerate(heap):
            heap[index] = element[1]
        
        return heap
            