class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_note_frequency = collections.Counter(ransomNote)
        magazine_frequency = collections.Counter(magazine)
        for char, frequency in ransom_note_frequency.items():
            if (char in magazine_frequency 
                and magazine_frequency[char] >= frequency):
                continue
            else:
                return False
        
        return True