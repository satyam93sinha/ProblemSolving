"""
Edge Cases:
1. The num given is less than 10; return the same num
2. The num given is greater than 10; keep adding the digits until we get the resultant digit/number less than 10

Approaches:
1. Brute Force
Intuition:
Add the num given and store/change the num itself with the sum of given num. Keep doing this until we get a single digit number.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            curr_sum = 0
            while num > 0:
                curr_sum += num % 10
                num //= 10
            num = curr_sum
            if num < 10:
                return num