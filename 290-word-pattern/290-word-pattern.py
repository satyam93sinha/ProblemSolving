class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        if len(set(pattern)) != len(set(s)):
            return False
        
        pattern_word_dict = {}
        for char, word in zip(pattern, s):
            if char not in pattern_word_dict:
                pattern_word_dict[char] = word
            else:
                if pattern_word_dict[char] == word:
                    continue
                else:
                    return False
        return True