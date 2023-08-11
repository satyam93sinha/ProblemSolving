class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 1
        
        for index, digit in enumerate(digits):
            digit += carry
            if digit > 9:
                digit = 0
                carry = 1
            else:
                carry = 0
            
            digits[index] = digit
        
        if carry:
            digits.append(carry)
        
        digits.reverse()
        
        return digits