"""
#### Edge Cases:
1. letters is empty; not possible, a constraint
2. len(letters) is at least 2 different chars, constraint;
    2.1 letters contain duplicates -> handle it
    2.2 letters do not contain duplicates -> doesn't matter already handling duplicates
    2.3 target is smallest in the letters so we have a char just greater than target
    2.4 target is largest in the letters so we have to use circle, return the smallest which comes after it (at index 0 because max is present at last index of letters)

#### Test Cases:
["c", "c", "d"]
"c"
["a", "b", "d"]
"b"
["c", "c", "f"]
"f"
["c","f","j"]
"d"
["c","f","j"]
"a"

#### Approaches:
1. Brute Force
Intuition:
Iterate over the letters array and search for the target, return letters[(target_index+1)%len(letters)] as answer
Time: O(n)
Space: O(1)

2. Letters array is sorted in ascending order, Use Binary Search
Intuition:
Maintain left and right pointers, reduce search space into half based on mid element and if target is found, we have to go right to find the last index it could be present at, because answer lies next to the target_element's last occurence. Later, outside while loop we can handle the 'z' -> 'a' case by returning letters[(target_index + 1) % len(letters)]
Time: O(logn)
Space: O(1)
"""


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        last_occurence = 0
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] == target:
                last_occurence = mid
                left = mid + 1
            elif letters[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if left == len(letters):
            return letters[0]
        return letters[left]