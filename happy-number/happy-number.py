class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            n = self.get_next_number(n)
        
        return n == 1
    
    def get_next_number(self, n: int) -> int:
        square_sum = 0
        while n > 0:
            last_digit = n % 10
            n //= 10
            square_sum += pow(last_digit, 2)
        return square_sum