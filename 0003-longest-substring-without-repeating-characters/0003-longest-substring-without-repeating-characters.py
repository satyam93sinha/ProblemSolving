"""
Edge Cases:
1. s can be empty; return 1 because there is no repeating char
2. len(s) > 1:
    a. s has all the chars repeated, same chars until len(s); return 1
    b. s has all the distinct chars; return len(s)
    c. s has mixed; find out length of the longest substring without any repeating char

Test Cases:
""
"aaaaaaa"
"abcdef"
"abcabcbb"
"pwwkew"

Approaches:
1. Brute Force
Intuition:
Iterate over string s, keep track of the chars that are already seen/visited(set), if its already seen and appears again, break the inner loop.
Time: O(n^2)
Space: O(len(s)) or O(longest unique chars in s)

2. Optimal
Intuition:
In the above approach, we revisit the already visited chars of string s, so is there a way to keep their calculations somehow to use in future iterations than re-calculating? Sliding Window
Time: O(n)
Space: O(n)
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = 0
        seen = set()
        length_longest_substring = 0
        while start <= end and end < len(s):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            
            length_longest_substring = max(length_longest_substring, end-start+1)
            seen.add(s[end])
            end += 1
        
        return length_longest_substring