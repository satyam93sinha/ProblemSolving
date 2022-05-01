​
#### Edge Cases:
1. Empty string:
i) no backspace nothing; return True
ii) only backspaces, return True
iii) made empty through backspaces; compare and return bool
2. Equal String:
i) s and t are simple string without backspaces
ii) s and t are made equal with backspaces
iii) s and t are made equal containing extra backspaces(backspaces on empty string too)
3. Non-equal string:
i) s and t are inequal, contain no backspaces
ii) s and t are inequal, contain backspaces but char are not equal
iii) s and t are inequal, backspaces made them inequal
​
#### Test Cases:
1. s = "", t = ""
2.i) s = "ab##", t = "c#d#"
2.ii) s = "##", t = "##"
3. s = "abc", t = "abc"
4. s = "a#c", t = "b"
5. s = "ab#c", t = "ad#c"
6. s = "ab##c", t = "ad#c", extra backspaces in empty text has empty text
​
#### Approach:
1. **Brute Force**
Intuition: Keep a stack for s and t and append elements until there's a "#" backspace character, once backspace is found, pop the last inserted element -> gives us the final string formed. Compare this string with that formed of t and return the answer
*Time: O(len(s) + len(t))
Space: O(len(s) + len(t)); for stack*
​
2. **Two Pointer**
Intuition: Iterate on characters in reverse order and skip char that appears before "#". Build a string through this and compare its reverse.
*Time: O(len(s) + len(t))
Space: O(len(s) + len(t))*
​
3. **Two Pointer, Space Optimized**
Intuition: Use Approach-2 with skip count and generator
*Time: O(len(s) + len(t))
Space: O(1)*
​