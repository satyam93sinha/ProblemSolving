"""
Edge Cases:
1. String is already a palindrome; return True
2. String is not a palindrome
    i) Either we can make it a palindrome by deleting at most one character
    ii) Or it can not be made a palindrome by deleting at most one character

Test Cases:
1. s = "aba"
2.i) s = "abca", delete any of b or c and it will be a palindrome
     s = "abcca", we need to delete b, how do we know it is to be deleted?
     s = "dadc", we need to delete c, how do we know which one is to be deleted?
     
How do we know which unmatching char is to be deleted?
Ans: Let's take the second example, "abcca", "a" and "a" match so we decrement start and end indices/pointers, "b" and "c" don't match so we can get a matching char either by incrementing start or decrementing end else this string can not be made a palindrome after single deletion.

Remember, there can only be one deletion!

Approaches:
1. Brute Force
Intuition: Delete every character once keeping others and check if the string becomes a palindrome, if it does return True else False.
Time: O(n^2) because in worst case we will end up looking for every character and the string may not be made a palindrome
Space: O(1) no extra space is being used

2. Optimised, two pointers
Intuition: We have to find an unmatching character and then check if the string can be made palindrome after removing that unmatching character from beginning or the end of the string. In order to check for a palindrome we keep a function check_palindrome passing in left, right pointers and string s itself. If it becomes a palindrome, we can return True else we don't need to delete any other character as the limit of deletion of characters is already exhausted.
Time: O(n)
Space: O(1)
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return (self.check_palindrome(left+1, right, s)
                        or self.check_palindrome(left, right-1, s))
        # the string s is already a palindrome, it won't enter else condition
        return True
    
    def check_palindrome(self, left: int, right: int, s: str) -> bool:
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
