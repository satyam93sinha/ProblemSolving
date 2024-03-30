"""
Edge Cases:
1. All the elements in the array are 0s; max_consecutive 1s = 0
2. All the elements in the array are 1s; max_consecutive 1s = length of the array
3. mixed 0s and 1s

Approaches:
1. Brute Force:
Nested for loop, outer one iterates over the elements, when 1 is found, we iterate the inner loop which keeps count of the ones stored in another variable. Lastly, return this variable as answer.
Time: O(n^2), Space: O(1)

2. Optimised:
Keep iterating over the nums array, if a 1 is found then increment the consecutive_1s, if a 0 is found, reset this consecutive_1s count to 0. Also, keep storing the max_consecutive_1s in this variable.
Time: O(n), Space: O(1)
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_1s = 0
        max_consecutive_1s = 0
        # iterate over the nums array
        for num in nums:
            if num == 1:
                consecutive_1s += 1
            else:
                consecutive_1s = 0
            max_consecutive_1s = max(max_consecutive_1s, consecutive_1s)
        
        return max_consecutive_1s