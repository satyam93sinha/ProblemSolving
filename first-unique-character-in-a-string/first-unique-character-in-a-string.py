
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_counter = collections.Counter(s)
        for index, char in enumerate(s):
            if s_counter[char] == 1:
                return index
        return -1