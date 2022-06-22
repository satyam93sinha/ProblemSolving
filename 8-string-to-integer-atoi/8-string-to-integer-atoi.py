class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        INT_MIN = -pow(2, 31)
        INT_MAX = pow(2, 31) - 1
        n = len(s)
        index = 0
        
        while index < n and s[index].isspace():
            index += 1
        
        if index < n and s[index] in {'-', '+'}:
            sign = -1 if s[index] == '-' else 1
            index += 1
        
        while index < n and s[index].isdigit():
            result = result*10 + ord(s[index]) - ord('0')
            index += 1
        result *= sign
        
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        return result