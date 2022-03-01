class Solution:
    def isHappy(self, n: int) -> bool:
        # Time: O(logn)
        # Space: O(1)
        def get_next_number(num):
            square_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                square_sum += pow(digit, 2)
            return square_sum
        
        # cycle members : {4, 16, 37, 58, 89, 145, 42, 20}
        # all the digit square of 4 form a cycle
        
        while n != 1 and n != 4:
            n = get_next_number(n)
        
        return n == 1