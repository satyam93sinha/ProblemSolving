"""
Edge Cases:
1. Array is rotated 0 or n times, it is in ascending order
2. Array is rotated 1 <= k < n times, normal case, work on it
3. Array has duplicates, constraint says array doesn't have duplicates
4. Array has single element

Test Cases:
1. [0, 1, 2, 3, 4] -> return 0; simple Binary Search would return the min element
2. [3, 4, 0, 1, 2] -> return 0; find pivot where neighbors are greater than mid
3. [4, 0, 1, 2, 3] -> return 0; go to unsorted part and when left == right, break

Approaches:
1. Brute Force -> Time: O(n), Space: O(1) :: Linear Search
2. Use Binary Search -> Time: O(logn), Space: O(1)
Intuition:
Maintain a left and right pointers, find a mid num or pivot which is less than its previous and next elements. Works only if Rotated Sorted Array has distinct elements.

Algorithm:
Step1 -> left, right = 0, len(nums) - 1
Step2 -> Iterate until left < right
Step3 -> Check if mid element is pivot, ensure to handle mid == 0 or mid == len(nums)-1. If so, break the loop or return this element as min element
Step4 -> Check if right half is sorted
Step4.1 -> If left half is sorted then, check if complete array is sorted by checking nums[left] <= nums[mid] <= nums[right]. If so, go towards left, right = mid else go right(is unsorted) right = mid + 1
Step4.2 -> Else check if left to right is sorted => right = mid ;; else, left = mid + 1
Step5 -> return left(here, left == right)
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                if nums[mid] <= nums[right]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] <= nums[right]:
                    right = mid
                # else:
                #     left = mid + 1
        return nums[left]
        
        
        