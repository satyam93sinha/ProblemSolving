"""
Edge Cases:
1. heights in ascending order
2. heights in descending order
3. heights are mixed and not sorted

Test Cases:
1. [1, 2, 3, 4, 5]; output = 6 (3 to 5 will be a container)
2. [5, 4, 3, 2, 1]; output = 6 (5 to 3 will be a container)
3. [1, 8, 6, 2, 5, 4, 8, 3, 7]; output = 49 (8 to 7 will be a container)

Approaches:
1. Brute Force
Intuition: Calculate area for every element with every other element and update the max_area water can be stored. 
How will this area be calculated?
Ans: Minimum of two heights in consideration multiplied by distance between them.
Time: O(n^2) considering every area
Space: O(1)

2. Two Pointers
Intuition: Keep track of left and right pointers and decrement them iff either of them are less than the other.
Time: O(n)
Space: O(1)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = float('-inf')
        while left <= right:
            current_area = min(height[left], height[right]) * (right-left)
            max_area = max(current_area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area