class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_frequency = collections.Counter(s)
        for index, char in enumerate(s):
            if char_frequency[char] == 1:
                return index
        return -1