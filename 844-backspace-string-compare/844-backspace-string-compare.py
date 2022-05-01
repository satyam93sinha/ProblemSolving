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

2. Two Pointer
Intuition: Iterate on characters in reverse order and skip char that appears before "#". Build a string through this and compare its reverse.
Time: O(len(s) + len(t))
Space: O(len(s) + len(t))

3. Two Pointer, Space Optimized
Intuition: Use Approach-2 with skip count and generator
Time: O(len(s) + len(t))
Space: O(1)

"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def F(string):
            skip_char = 0  # skip a char due to backspace
            for char in reversed(string):
                if char == "#":
                    skip_char += 1
                elif skip_char:  # char is being skipped so decrementing it to make it back to 0
                    skip_char -= 1
                else:  # char to be considered
                    yield char
        
        return all(char_s == char_t for char_s, char_t in itertools.zip_longest(F(s), F(t)))