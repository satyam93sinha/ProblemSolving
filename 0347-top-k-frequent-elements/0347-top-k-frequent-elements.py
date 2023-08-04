class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = collections.Counter(nums)
        
        min_heap = []
        
        for num, frequency in nums_counter.items():
            heapq.heappush(min_heap, (frequency, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        answer = [num for freq, num in min_heap]
        
        return answer