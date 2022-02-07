"""
Edge Cases:
1. char is present in s but not in t; return the difference char
2. char is present in both s and t and is an extra
3. empty string s, but t contains a char

Test Cases:
1. s = "abcd", t = "abcde"
2. s = "aaa", t = "aaaa"
3. s = "", t = "a"

Approaches:
1. Brute Force, Use Sorting
Time: O(nlogn)
Space: O(n) for storing sorted string
Intuition:
When the string is sorted, we can compare every element in both the strings and if we find a char that is not equal to the other, is an extra char.

2. Use Hashing
Time: O(n)
Space: O(1) length of dictionary never exceeds 26 bcoz there are total 26 small/capital letters in English Alphabet.
Intuition:
Maintain a char_freq dictionary that contains char and its frequency in s. When this char's frequency reaches zero and it is encountered again, it is the difference char else if char is not present in s or the dictionary, it is the difference char.
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Time: O(n), Space: O(1)
        char_freq_s = collections.Counter(s)
        for char in t:
            if char in char_freq_s:
                if char_freq_s[char] == 0:
                    return char
                else:
                    char_freq_s[char] -= 1
            else:
                return char
        
        """
        # Time: O(nlogn), Space: O(n)
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        for s_iter in range(len(s)):
            if sorted_s[s_iter] != sorted_t[s_iter]:
                return sorted_t[s_iter]
        
        # we compared until len(s)-1,
        # remaining is last element of sorted_t or t
        return sorted_t[-1]
        """
        