class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        ceil = -1
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] == target:
                ceil = mid + 1
                left = mid + 1
            elif letters[mid] > target:
                ceil = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if ceil == -1 or ceil == len(letters):
            return letters[0]
        else:
            return letters[ceil]