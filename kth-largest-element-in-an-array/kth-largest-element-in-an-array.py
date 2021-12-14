'''
Edge Cases:
1. Array is sorted in ascending order -> return (n-k)th element of the array
2. Array is sorted in descending order -> return (k)th element of the array
3. Normal unsorted array
4. Same number as duplicates in the array
5. Single element in the array
6. Empty array

Brute Force:   Time - O(nlogn), Space - O(1)
Sort the array and then return (n-k)th element in all the cases.

2nd Approach:   Time - O(nlogk), Space - O(k) for heap
Maintain a min-heap of size k, inserting new element that is less than root node and popping up the root node. At the end of the array iteration we would have kth largest element at the root node of heap.

Optimised Approach: Use Quick Select Algorithm (a Divide n Conquer approach)
Time - O(n), worst-case - O(n^2) rarely encountered, 
Space - O(n)  due to recursion
Divide the array in left and right half based on pivot_index returned from partition method call. When pivot_index == n-k, we found kth largest element.
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_divide(nums, 0, len(nums) - 1, len(nums) - k)
    
    def quick_divide(self, nums: List[int], start: int, end: int, k: int):
        if start > end:  # base condition
            return 0
        partition_index = self.partition(nums, start, end)
        if partition_index == k:
            return nums[partition_index]
        elif partition_index < k:
            # go right
            return self.quick_divide(nums, partition_index + 1, end, k)
        else:
            # go left
            return self.quick_divide(nums, start, partition_index - 1, k)
        
    def partition(self, nums: List[int], start: int, end: int):
        pivot_index = start
        random_index = random.randint(start, end)
        nums[random_index], nums[end] = nums[end], nums[random_index]
        pivot = nums[end]
        
        while start < end:
            if nums[start] < pivot:
                nums[start], nums[pivot_index] = nums[pivot_index], nums[start]
                start += 1
                pivot_index += 1
            else:
                start += 1
        nums[pivot_index], nums[end] = pivot, nums[pivot_index]
        return pivot_index
        
        
        