class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        hashset = set()
        start, end = 0, 0
        while start <= end and end < len(s):
            while s[end] in hashset:
                hashset.remove(s[start])
                start += 1
            hashset.add(s[end])
            end += 1
            longest_length = max(longest_length, end-start)
        
        return longest_length