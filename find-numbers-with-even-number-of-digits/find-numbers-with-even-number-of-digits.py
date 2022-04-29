class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit_nums = 0
        for num in nums:
            count_digits = 0
            while num:
                num //= 10
                count_digits += 1
            if count_digits % 2 == 0:
                even_digit_nums += 1
        
        return even_digit_nums