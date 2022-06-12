"""
#### Edge Cases:
1. Empty array nums; return -1
2. Single element array; return index if found else -1
3. len(nums) >= 2; find the element and return index
    3.1 nums can be sorted completely in ascending order, 0 rotations
    3.2 nums is rotated by k

#### Test Cases:
[]
3
[5, 1, 3]
3
[3]
3
[3]
4
[1, 2, 3, 4]
2
[1, 2, 3, 4]
5
[3, 4, 1, 2]
1
[4, 1, 2, 3]
5

#### Approaches:
1. **Brute Force**
Intuition:
Iterate over the whole nums array and check if the target is found
Time: O(n)
Space: O(1)

2. **Use Binary Search :: array is sorted and rotated :: Two passes**
Intuition:
Find pivot element, index where array is rotated or min of nums array.
Search for element in 0->pivot, pivot and pivot->len(nums) in O(logn) using binary search providing indices, array and target to the binary search function
Time: O(logn) -> 2 times
Space: O(1)

3. **Use Binary Search :: Single pass**
Intuition:

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            # right half should be sorted
            else:
                # check target present in right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        if nums[left] != target:
            left = -1
        return left