"""
Edge Cases:
1. s == t; return True
2. s != t; check if s is a subsequence of t and return accordingly
    a) s > t; return False
    b) s < t; return False

Approaches:
1. Brute Force
Intuition:
Find all the subsets/subsequences of t and then check if s matches any one of them.
Time: O(2^n) for generating all the subsets of t
Space: O(2^n) for storing all the subsets of t, we can reduce it to O(n) for call stack if we match s with the subsets while generating them

2. Optimised
Intuition:
If anyhow we know the elements present in s are in the same order in t. First, lets check if any element in s is not present in t -> it can not be a subsequence(return False)
Second, iterate over s and maintain an index that sees the element present in t is in the same order as s
Time: O(len(t)) storing char of t's index and count in a dictionary
Space: O(len(t)) dictionary storing t char's index and count/frequency

3. Simple and Optimised, Two Pointers
Intuition:
Maintain two pointers one for s and another for t, if char in t equals s char we increment s_position else keep checking this, whenever s_position reaches its length, we know that s is a subsequence of t.
Time: O(len(t))
Space: O(1)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_position = 0
        for index, char in enumerate(t):
            if s_position < len(s) and char == s[s_position]:
                s_position += 1
        if s_position == len(s):
            return True
        else:
            return False