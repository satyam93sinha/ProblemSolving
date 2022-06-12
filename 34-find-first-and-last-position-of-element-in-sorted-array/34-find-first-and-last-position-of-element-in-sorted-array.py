"""
Edge Cases:
Array is already sorted in non-decreasing order
1. len(nums) == 0, empty array; return [-1, -1]
2. len(nums) == 1, if it is the element return [0, 0] else [-1, -1]
3. len(nums) >= 2,
    3.1 number is found, we can return [first, last] indices
    3.2 number is not found, return [-1, -1]
    3.3 array has only given number as elements, return [0, len(nums)-1]

Test Cases:
[]
3
[3]
3
[1, 2, 3, 4, 5]
2
[1, 2, 2, 2, 3]
2
[1, 2, 2, 3]
4
[1, 1, 1]
1

Approaches:
1. Brute Force
Intuition:
Iterate over the whole array and store first and last occurences in a variable/list, return that list
Time: O(n)
Space: O(1)

2. Use Binary Search :: Why? -> Array is already sorted
Intuition:
Search for the number, if found keep reducing the search space to first half and store the index in first occurence. Similarly, search for the index of the element in second half.
Time: O(logn)
Space: O(1) -> use loop for binary search, if recursion is used, O(logn) space complexity due to recursion stack

"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_occurence = self.first_occurence(nums, target)
        last_occurence = self.last_occurence(nums, target)
        return [first_occurence, last_occurence]
    
    def first_occurence(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        first_occurence = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
                first_occurence = mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return first_occurence
    
    def last_occurence(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        last_occurence = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
                last_occurence = mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return last_occurence