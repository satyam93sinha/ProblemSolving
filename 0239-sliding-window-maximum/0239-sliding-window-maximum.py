class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        max_numbers = []
        start = end = 0
        
        while start <= end and end < len(nums):
            # calculations
            heapq.heappush(heap, [-nums[end], end])
            if end-start+1 < k:
                end += 1
            # end-start+1 == k
            elif end-start+1 == k:
                # answer <- calculations
                max_numbers.append(-heap[0][0])
                # remove nums[start] from calculations
                while heap and start >= heap[0][1]:
                    heapq.heappop(heap)
                
                # slide the window
                start += 1
                end += 1
        return max_numbers