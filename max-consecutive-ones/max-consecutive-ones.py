"""
Edge Cases:
1. nums array is empty; not possible, a constraint
2. nums array contain no 1; not possible, a constraint
3. nums array contain 1s
    i) all the 1s are consecutive; return length of nums array
    ii) no 1s are consecutive; alternate 1s and 0s; return count = 1
4. nums array contain both 1s and 0s
    i) consecutive 1s are separated by 0s; need to compute max consecutive 1s; multiple consecutive 1s
    ii) there is only one consecutive 1s in the array

Test Cases:
[1,1,0,1,1,1]
[1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1]
[1,1,1,1]
[1,0]
[1,0,1,0,1,0]

Approaches:
1. Brute Force
Intuition:
Iterate over every 1 and find the consecutive 1s count from it, store max consecutive 1s in a variable
Time: O(n^2)
Space: O(1)

2. Optimised
Storing count of 1s in consecutive_1s variable and resetting it on encountering 0s and maintaining max_consecutive_1s
Time: O(n)
Space: O(1)
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive_1s = 0
        max_consecutive_1s = float('-inf')  # it can also be 0, because there won't be negative counts
        for num in nums:
            if num:  # num == 1
                consecutive_1s += 1
            else:
                consecutive_1s = 0
            max_consecutive_1s = max(max_consecutive_1s, consecutive_1s)
        
        return max_consecutive_1s
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        consecutive_1s = 0
        max_consecutive_1s = 0
        for num in nums:
            if num == 1:
                consecutive_1s += 1
                max_consecutive_1s = max(max_consecutive_1s, consecutive_1s)
            else:
                consecutive_1s = 0
            
        return max_consecutive_1s
        """