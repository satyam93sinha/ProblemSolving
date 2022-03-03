"""
Edge Cases:
1. len(nums) < 3; return 0; there must be atleast 3 elements for it to be arithmetic
2. whole nums array is arithmetic; return len(nums)
3. a part of nums array is arithmetic; return the length
4. there are multiple arithmetics in nums array
5. all elements are equal

Test Cases:
1. [1,2] or [1]; return 0
2. [1, 2, 3, 4]; return 4 for [1, 2, 3, 4]
3. [10, 20, 30, 50]; return 3 for [10, 20, 30]
4. [1, 2, 3, 5, 6, 7, 8, 15, 9, 10, 11]; return [1,2,3], [5,6,7,8], [9,10,11]
5. [8, 8, 8, 8]

Approaches:
1. Brute Force
Intuition:
Generate all the subarrays of given nums list and check for arithmetic among them.
Time: O(2^n * n) to create all possible subarrays and then check for arithmetic ones
Space: O(2^n) to store all the possible subarrays
"""

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        cur_diff, cnt = -1, 0
        res = 0
        for i in range(1, len(nums)):
            new_diff = nums[i] - nums[i-1]
            if new_diff != cur_diff:
                cur_diff, cnt = new_diff, 1
            else:
                res += cnt
                cnt += 1
        return res