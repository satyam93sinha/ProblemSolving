"""
Edge Cases:
1. The num given is less than 10; return the same num
2. The num given is greater than 10; keep adding the digits until we get the resultant digit/number less than 10

Approaches:
1. Brute Force
Intuition:
Add the num given and store/change the num itself with the sum of given num. Keep doing this until we get a single digit number.
Time: O(logn)
Space: O(1)

2. Mathematical : Digital Root
Intuition:
Search for digital root formula.
To compute a digital root in a decimal numeral system,
digital_root(base10)(n) = 0, if n == 0
digital_root(base10) (n) = 9, if n == 9k, number n is divisible by 9
digital_root(base10) (n) = n mod 9, if n != 9k, number n is not divisible by 9.

Time: O(1)
Space: O(1)
"""

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
        
        """
        while True:
            curr_sum = 0
            while num > 0:
                curr_sum += num % 10
                num //= 10
            num = curr_sum
            if num < 10:
                return num
        """