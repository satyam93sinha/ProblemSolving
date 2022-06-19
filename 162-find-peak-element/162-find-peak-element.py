"""
#### Edge Cases:
1. nums is empty; no peak element
2. len(nums) >= 1; find the peak
    2.1 len(nums) == 1; the only num present in nums is answer
    2.2 nums is sorted in ascending order; last element is peak
    2.3 nums is sorted in descending order; first element is peak
    2.4 nums form a/many mountain peaks, nums is not sorted
    2.5 nums has same elements throughout the array; a constraint
    2.6 handle index == 0 and index == len(nums) when looking out for peak element
    
#### Test Cases:
[]
[1]
[1, 2, 3, 4]
[4, 3, 2, 1]
[1, 2, 3, 1, 5, 2]

#### Approaches:
1. **Brute Force**
Intuition:
Iterate over the whole nums array and find the peak, when found return the index
*Time: O(n)
Space: O(1)*

2. **Use Binary Search**
Intuition:
Find mid element and check if it is a peak, else go towards the half where mid's next element is greater than mid. We can modify the array by appending -math.inf at the end to handle mid == 0 and mid+1 == len(nums), IndexError handling.
*Time: O(logn)
Space: O(1)*
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # single element
        if len(nums) == 1:
            return 0
        # first element is peak
        if nums[0] > nums[1]:
            return 0
        # last element is peak
        if nums[-1] > nums[-2]:
            return len(nums)-1
        
        left, right = 1, len(nums)-2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        return -1