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

2. Using Heap - Time: O(nlogk + k), Space: O(k)
Use a max heap to store points basis their distance from origin and pop the max distance point to insert less distance iff length of heap reaches k. Then, return heap[:k] removing the distance part

3. Using Quick Select/Hoare's Algorithm -
Time: O(n) in best and average case, O(n**2) in worst case which is rarely seen
Space: O(n) if considering recursion call stack, else O(1)
"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points
        return self.quick_divide(points, 0, len(points)-1, k)
    
    def quick_divide(self, points, start, end, k):
        if start <= end:
            partition_index = self.partition(points, start, end)
            if partition_index == k:
                return points[:k]
            elif partition_index > k:
                return self.quick_divide(points, start, partition_index-1, k)
            else:
                return self.quick_divide(points, partition_index + 1, end, k)
    
    def partition(self, points, start, end):
        random_index = random.randint(start, end)
        points[random_index], points[end] = points[end], points[random_index]
        pivot = points[end]
        pivot_distance = math.sqrt(pow(0 - pivot[0], 2) + pow(0 - pivot[1], 2))
        pivot_index = start
        while start < end:
            distance = math.sqrt(pow(0 - points[start][0], 2) 
                                 + pow(0 - points[start][1], 2))
            if distance <= pivot_distance:
                points[pivot_index], points[start] = points[start], points[pivot_index]
                pivot_index += 1
            start += 1
        
        # place pivot at its correct position
        points[pivot_index], points[end] = points[end], points[pivot_index]
        return pivot_index
            