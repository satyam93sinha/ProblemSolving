import heapq

class Solution:
    def thirdMax(self, nums: "List[int]") -> int:
        heap = []
        # nums = set(nums)
        for num in nums:
            # O(3) ==> O(1) time operation
            if num not in heap:
                heapq.heappush(heap, num)
            if len(heap) > 3:
                heapq.heappop(heap)

        return heap[0] if len(heap) == 3 else max(heap)