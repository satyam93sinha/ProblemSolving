class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_of_digits = 0
        product_of_digits = 1
        while n > 0:
            remainder = n % 10
            sum_of_digits += remainder
            product_of_digits *= remainder
            n //= 10
        
        return product_of_digits - sum_of_digits