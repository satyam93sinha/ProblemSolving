"""
Edge Cases:
1. arr is empty; not possible, a constraint
2. len(arr) == 1; return [-1]
3. arr is sorted in ascending order; last element will be the greatest element on right
4. arr is sorted in desceding order
5. arr is not sorted

Test Cases:
[]
[4]
[1, 2, 3, 4]
[4, 3, 2, 1]
[17, 18, 5, 4, 6, 1]

Approaches:
1. Brute Force
Intuition:
Iterate over the array from beginning to the end and for every element we run an inner loop to find the maximum/greatest element towards the right of outer loop's element. When we find the greatest element we place it at the current index. Every time the last index will have -1 because there is/will be no element greater than it towards right.
Time: O(n^2)
Space: O(1)

2. Use Stack
Intuition:
As we iterate from current element to the right end of the array to find the greatest number towards right, we may use stack to do it for us(referring to Aditya Verma's stack playlist => deduction of ways to solve a stack problem/when to know to use stack in a problem). So let's iterate from the end and store the maximum element found in the stack. We would only be storing the maximum element found so far while iterating from end to beginning of the stack.
Time: O(n)
Space: O(1) -> length of this stack will never exceed 1 because there can only be one greatest/maximum number.

3. Use a variable to store maximum number, not a stack
Intuition:
In Approach-2 albeit we use stack, we are actually storing only one element in it so it's possible to store this value into a variable than a stack data structure keeping runtime complexity linear and constant space.
Time: O(n)
Space: O(1) -> no extra data structure used, only one variable that stores the maximum value found towards right.
"""

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum_value_right = -1
        for index in range(len(arr)-1, -1, -1):
            arr[index], maximum_value_right = maximum_value_right, max(maximum_value_right, arr[index])
        return arr