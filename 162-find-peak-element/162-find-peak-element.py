"""
Edge Cases:
1. nums array is in ascending order; return last element as peak element
2. nums array is in descending order; return first element as peak element
3. Normal case: Array is not sorted
    i) There are multiple peak elements, return any of them
    ii) There is single peak element, return it
4. Single length nums array -> return the only element as peak element

Approaches:
1. Brute Force
Time: O(n) iterate through the array and find the element which is greater than its neighbours
Space: O(1)

2. Use Binary Search
Time: O(logn)
Space: O(1)
Intuition: find a way to shift left or right and return the peak element if it satisfies the condition of being peak element
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # handling the edge cases, without altering the array
        # Edge Case: single element in nums array
        if len(nums) == 1:
            return 0
        # Edge Case2: if first element is peak element
        if nums[0] > nums[1]:
            return 0
        # Edge Case3: if last element is peak element
        if nums[-1] > nums[-2]:
            return len(nums)-1
        # Edge Case4: Search for peak element in range(1, len(nums)-1)
        left, right = 1, len(nums)-2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
        
        
        
        """
        nums.append(float('-inf'))
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            # check if mid element is a peak element
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            # mid element is not a peak element then, 
            # check which of the neighbors do not fulfill the condition
            # for mid to be peak and go towards that half of the array
            elif nums[mid-1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        """
        
        