"""
Edge Cases:
1. Length of pattern and that of s.split() don't match, there are extra words or characters in either of s or pattern; return False
2. Pattern and words in s follow a full match according to the question
3. Pattern and words in s do not follow a full match

Test Cases:
1. pattern = "abba", s = "dog cat cat dog dog cat cat dog"; return False
2. pattern = "ab", s = "dog cat"; return True
3. pattern = "abba", s = "dog cat cat fish"; return False
   pattern = "abba", s = "dog dog dog dog"; return False

Approaches:
1. Brute Force using two hashmaps
Intuition: Handle the test case of difference in length and return False. Map character to word and words to their respective characters so that we can handle the last test case without fail by checking their respective mapping match.
Time: O(n)
Space: O(m) for number of unique words present in s

2. Brute Force Using a hashset and one hashmap
Intuition: Handle the test case of difference in length and return False in O(1) time. Map character to word and if they keep matching continue doing this else when character is already present in the dictionary but word being encountered is not what is expected/seen earlier we can return False because it is not a full match adhering to the problem statement.
To handle Test Case3, pattern = "abba", s = "dog dog dog dog", we can compare the len(set(pattern)) != len(set(s.split())) if they don't match there is no full match.
Time: O(n)
Space: O(m) for set(s.split()) else, set(pattern) and dictionary mapping of char to words will be O(1) as there can not be more than O(26) characters.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        map_char = {}
        map_word = {}
        
        for char, word in zip(pattern, s):
            if char not in map_char:
                map_char[char] = word
            else:
                if map_char[char] != word:
                    return False
            if word not in map_word:
                map_word[word] = char
            else:
                if map_word[word] != char:
                    return False
        
        return True
            
            