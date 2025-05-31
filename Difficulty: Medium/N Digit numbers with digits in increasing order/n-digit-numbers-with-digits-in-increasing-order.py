
from typing import List


class Solution:
    def __init__(self):
        self.result = []
    def increasingNumbers(self, n : int) -> List[int]:
        # code here
        if n == 1:
            return [num for num in range(0, 10)]
        number = [0 for _ in range(n)]
        for num in range(1, 10):
            number[0] = num
            self.form_numbers(number, n-1, 1)
            
        return self.result
    
    def form_numbers(self, number: List, n: int, index: int) -> None:
        if n == 0:
            self.result.append(int(''.join([str(num) for num in number])))
            return
        last_digit = number[index-1]
        for num in range(last_digit+1, 10):
            number[index] = num
            self.form_numbers(number, n-1, index+1)
            # number[index] = 0  # backtracking isn't necessary, overwrite handles
        return
            
        
