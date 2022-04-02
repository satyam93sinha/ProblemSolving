class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_index, num2_index = len(num1)-1, len(num2)-1
        sum_ = ''
        carry = 0
        while num1_index > -1 or num2_index > -1:
            current_sum = carry
            if num1_index > -1:
                current_sum += int(num1[num1_index])
                num1_index -= 1
            if num2_index > -1:
                current_sum += int(num2[num2_index])
                num2_index -= 1
            
            carry = current_sum // 10
            current_sum %= 10
            
            sum_ += str(current_sum)
        
        if carry:
            sum_ += str(carry)
        
        return sum_[::-1]