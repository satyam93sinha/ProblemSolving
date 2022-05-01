"""
Edge Cases:
1. Empty string; no backspace nothing; return True
2. Empty string
    i) string made empty by backspacing or deleting characters
    ii) string is empty and only backspacing is found in the given string
3. s and t are simple string without backspacing and is equal
4. eventually, s != t; return False
5. s == t after usage of some backspaces

Test Cases:
1. s = "", t = ""
2.i) s = "ab##", t = "c#d#"
2.ii) s = "##", t = "##"
3. s = "abc", t = "abc"
4. s = "a#c", t = "b"
5. s = "ab#c", t = "ad#c"

Approach:
1. Brute Force
Intuition: Keep a stack for s and t and append elements until there's a "#" backspace character, once backspace is found, pop the last inserted element -> gives us the final string formed. Compare this string with that formed of t and return the answer
Time: O(len(s) + len(t))
Space: O(len(s) + len(t)); for stack

"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if s == t:  # edge case
            return True
        stack_s = []
        stack_t = []
        for char in s:
            if char == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(char)
        
        for char in t:
            if char == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(char)
        print(stack_s, stack_t)
        return stack_s == stack_t