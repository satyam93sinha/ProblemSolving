"""
Edge Cases:
1. heights is empty; not possible, a constraint
2. len(heights) == 1; return 0, no change in expected or heights as there is single element
3. len(heights) > 2; find the difference and return the answer
    i) heights contain same number as its elements
    ii) heights contain distinct numbers as its elements
    iii) len(set(heights)) >= 2
4. heights and expected are same; return 0

Test Cases:
[1, 1, 1, 1]
[1, 2, 3, 4]
[4, 3, 2, 1]
[1, 2, 1, 1]
[1]

Approaches:
1. Brute Force
Intuition:
Make a copy of heights array and sort it to get the expected array. Then, compare both of them, whichever index do not match, increment result or difference and return it eventually
Time: O(100 x log100), according to the constraint we can not have more than 100 elements in the heights array thus, it will be a constant time operation. Sorting won't exceed O(100log100) => O(1). In other words, O(nlogn) where 1 <= n <= 100.
Space: O(100) according to the constraint the number of elemtns in heights array can not exceed 100 thus, O(1) space complexity. In other words, O(n) where 1 <= n <= 100.

2. Optimised, use counting sort
Intuition:
Make an array of size 100 or max value from the heights array and keep the frequency of the elements as values at those indices. Thus, this extra space will never go beyond length - 100 leading to O(100) => O(1) constant space. Later, iterate through heights array and subtract/decrement the frequency of that number. Also, keep count of the differences/result.
Time: O(100) according to the constraints. In other words, O(n) where 1 <= n <= 100
Space: O(100) according to the constraints. In other words, O(n) where 1 <= n <= 100
"""


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        frequency_heights = [0 for _ in range(101)]
        
        for height in heights:
            frequency_heights[height] += 1
        
        current_height = 0
        result = 0
        
        for index, height in enumerate(heights):
            while frequency_heights[current_height] == 0:
                current_height += 1
            
            if current_height != height:
                result += 1
            
            frequency_heights[current_height] -= 1
        
        return result
        
        
        
        '''
        expected = heights.copy()
        expected.sort()
        different_indices = 0
        for height, expect in zip(heights, expected):
            if height != expect:
                different_indices += 1
        
        return different_indices
        '''