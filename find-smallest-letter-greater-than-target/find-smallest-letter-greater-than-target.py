"""
Edge Cases:
1. Letter is present ->
   i) no greater element present, wrap around and return the first element from letters
   ii) greater element present, return the next greater element
2. Letter is absent ->
   i) next greater is present
   ii) next greater is not present in straight way so wrap around and return the first element of letters
"""


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        next_alphabet = ''
        left, right = 0, len(letters)-1
        
        while left <= right:
            mid = (left + right) // 2
            if target < letters[mid]:
                next_alphabet = letters[mid]
                right = mid - 1
            else:
                left = mid + 1
        
        if next_alphabet == '':
            return letters[0]
        else:
            return next_alphabet