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

2. Less Lines of Code :: Credit -> Leetcode's solution
Intuition:
In our earlier approach we maintained everything to tell us if the array is valid mountain or not. Here, we can simply walk the isle/array and trust it to be valid mountain array. If it's not trustworthy/not valid mountain array we return False
Time: O(n)
Space: O(1)
"""


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Edge Case
        if len(arr) < 3:
            return False
        
        strictly_increasing = False
        strictly_decreasing = False
        index = 0
        
        # for strictly increasing
        while index+1 < len(arr) and arr[index] < arr[index+1]:
            index += 1
            strictly_increasing = True
        
        if not strictly_increasing:
            return False
        
        # for strictly decreasing
        while index+1 < len(arr) and arr[index] > arr[index+1]:
            index += 1
            strictly_decreasing = True
        
        if strictly_increasing and strictly_decreasing and index == len(arr)-1:
            return True
        
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        # Approach2
        index = 0
        # walk the strictly increasing array
        while index+1 < len(arr) and arr[index] < arr[index+1]:
            index += 1
        
        # peak element can not be start or end of the array
        # it means the array is either only strictly increasing or strictly decreasing
        if index == 0 or index == len(arr) - 1:
            return False
        
        # walk the isle/striclty decreasing array
        while index+1 < len(arr) and arr[index] > arr[index+1]:
            index += 1
        
        # two cases arise,
        # 1. the array is valid mountain array => index == len(arr)-1
        # 2. the array is not a valid mountain array => index != len(arr)-1 => index < len(arr)-1, which again implies that we have some elements that could be increasing or not striclty decreasing thus, not a valid mountain array
        return index == len(arr) - 1
        """
        
        """
        Approach1:
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
        """
            