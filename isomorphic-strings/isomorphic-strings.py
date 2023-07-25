class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map_s = {}
        char_map_t = {}
        for char_s, char_t in zip(s, t):
            if ((char_s in char_map_s and char_map_s[char_s] != char_t)
                or (char_t in char_map_t and char_map_t[char_t] != char_s)):
                return False
            char_map_s[char_s] = char_t
            char_map_t[char_t] = char_s
        return True