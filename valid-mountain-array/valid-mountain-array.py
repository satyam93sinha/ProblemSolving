"""
Edge Cases:
1. length of array is less than 3; return False
2. len(array) >= 3;
    2.1. array is a mountain array, strictly increasing then strictly decreasing
    2.2. array is not a mountain array, not strictly increasing/not strictly decreasing

Test Cases:
# Edge Case 1.
[1, 2]
# Edge Case 2.
[1, 2, 3, 4, 3, 2, 1]
[1, 2, 2, 3, 2, 1]
[1, 2, 3, 3, 2]
[1, 2, 3, 4]
[4, 3, 2, 1]
[1, 2, 1, 3, 4]

Approaches:
1. Brute Force
Intuition:
Maintain increasing and decreasing flags and check first for increasing flag if it gets to be true, we have already worked out the first half of the problem, work on second half. Ensure, we do not have any increasing case in the second half of determining strictly decreasing scenario.
Time: O(n)
Space: O(1)
"""


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        increasing_flag = False
        decreasing_flag = False
        iter_index = 1
        # checking for strictly increasing case
        for index in range(1, len(arr)):
            if arr[index] > arr[index-1]:
                increasing_flag = True
            else:
                iter_index = index
                break
        # edge case when we did not find strictly increasing elements
        if not increasing_flag:
            return False
        
        # checking for strictly decreasing case
        for index in range(iter_index, len(arr)):
            if arr[index] < arr[index-1]:
                decreasing_flag = True
            else:
                return False
        
        if increasing_flag and decreasing_flag:
            return True
        
        return False
            