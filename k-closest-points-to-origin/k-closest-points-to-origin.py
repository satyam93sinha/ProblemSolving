"""
Edge Cases:
1. closest points found be in decreasing order
2. closest points found is in ascending order
3. no closest point found
4. only one element
5. k == n

Approaches:
1. BRUTE FORCE- Time: O(nlogn), Space: O(1)
Sort the points array in increasing order using list's inbuilt sort method. The sorting is done on math.sqrt((0-x)**2 + (0-y)**2) distances.

2. Using Heap - Time: O(nlogk), Space: O(k)
Use a max heap to store points basis their distance from origin and pop the max distance point to insert less distance one iff length of heap reaches k


"""

from heapq import heappush, heappop


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point[0], point[1]
            distance = math.sqrt(pow(0-x, 2) + pow(0-y, 2))
            heappush(heap, (-distance, point))
            if len(heap) > k:
                heappop(heap)
        
        for index, element in enumerate(heap[:k]):
            heap[index] = element[1]
        
        return heap[:k]
            
            