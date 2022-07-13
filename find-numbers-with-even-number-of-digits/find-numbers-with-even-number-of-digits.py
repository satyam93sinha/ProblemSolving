class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        num_with_even_digits = 0
        for num in nums:
            count = self.count_of_digits(num)
            if count % 2 == 0:
                num_with_even_digits += 1
        
        return num_with_even_digits
    
    def count_of_digits(self, num: int) -> int:
        count_digits = 0
        while num > 0:
            count_digits += 1
            num //= 10
        
        return count_digits