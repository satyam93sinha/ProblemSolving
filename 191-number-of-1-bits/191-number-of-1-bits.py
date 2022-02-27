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

2. Bit Manipulation
Intuition:
There should be a number with which bit manipulated gives us count of 1s or single 1 in given number n.
Example:
n = 11 => 1011
n-1 = 10 => 1010
If we observe carefully, we can get count of least significant bit 1 by ANDing n and (n-1).
Time: O(1) just like above
Space: O(1) no extra space is used here
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        count_1s = 0
        while n != 0:
            count_1s += 1
            # gets n = n and n-1; 11 and 10; 
            # 1011 & 1010 => 1010; count = 1
            # 1010 & 1001 => 1000; count = 2
            # 1000 & 0111 => 0000; count = 3
            n &= (n-1)
        return count_1s
        
        
        
        """
        n = bin(n)[2:]
        count_1s = 0
        for char in n:
            if char == '1':
                count_1s += 1
        return count_1s
        """