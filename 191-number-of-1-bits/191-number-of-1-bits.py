"""
Edge Cases:
1. n = 0; return 0
2. n = 1; return 1
3. n > 1; return count of 1s in binary representation of n

Approaches:
1. Brute Force
Intuition:
Use inbuilt binary representation of a number and convert number to its bin. Iterate over the bin and count total number of 1s.
Time: O(bin(n)) => O(32) => O(1)
Space: O(bin(n)) => O(32) => O(1)
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        count_1s = 0
        for char in n:
            if char == '1':
                count_1s += 1
        return count_1s