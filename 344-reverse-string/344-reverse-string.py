"""
Edge Cases:
1. single char; len(s) == 1; do nothing
2. empty array; do nothing
3. len(s) > 1; reverse string

Approaches:
1. Brute Force
Time: O(n) iterate over s in reverse manner and append chars to result array
Space: O(n) use extra space for answer

2. Use Recursion
Time: O(n**2) decide to pop elements which reduces the input size and then, append them in Induction step eventually reversing the array of string
Space: O(n) recursion call stack, no other extra space used

3. Use Recursion
Time: O(n) use two pointer through recursion
Space: O(n) recursion call stack

4. Use Two Pointer
Time: O(n)
Space: O(1)
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Two Pointer Approach : optimised approach
        start, end = 0, len(s)-1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        
        """
        # Two Pointer approach using Recursion
        def helper(start=0, end=len(s)-1):
            # base condition
            if start >= end:
                return
            # hypothesis
            # swap
            s[start], s[end] = s[end], s[start]
            # recursively call
            helper(start+1, end-1)
        
        helper()
        """
        
        """
        # base condition
        if len(s) == 0:
            return
        else:
            # hypothesis
            pop_char = s.pop()
            self.reverseString(s)
            
            # induction, insert at beginning
            # insertion at beginning takes O(n) time in an array
            s.insert(0, pop_char)
        """