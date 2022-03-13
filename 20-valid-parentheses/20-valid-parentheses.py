"""
Edge Cases:
1. Empty string; not possible, a constraint
2. length == 1; return False
3. length > 1; check for balanced parentheses

Approaches:
1. Use stack
Intuition:
Put every open bracket into Stack and once we encounter a closed bracket we keep popping until we find respective open bracket else parentheses is not balanced.
Time: O(n)
Space: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces_dict = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char not in braces_dict:
                stack.append(char)
            elif stack and stack[-1] == braces_dict[char]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        else:
            return True