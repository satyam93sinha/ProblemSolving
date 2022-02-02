"""
Edge Cases:
1. p's anagrams are not present in s
2. p's anagrams are present in s
    i) p == s
    ii) s contains p
    iii) normal case to find anagrams of p in s

Approaches:
1. Brute Force
Time: O(len(s) * len(p))
Space: O(len(p)) for storing the char and its frequency of p in dictionary
Intuition:
Store char and its frequency for p in p_freq_dict in O(len(p)) time and space.
Iterate through s checking for p's anagrams in time O(len(s)*len(p))

2. Sliding Window
Time: O(len(s) + len(p))
Space: O(len(p)) for storing char and freq of p in dictionary
Intuition:
Store p's char and freq in p_freq_dict in O(len(p)) time and space.
Maintain a start and end while iterating through s's chars
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_freq = collections.Counter(p)
        length = 0
        start, end = 0, 0
        curr_char_freq = {}
        output = []
        
        while start <= end and end < len(s):
            char = s[end]
            if char in p_freq:
                if char not in curr_char_freq:
                    curr_char_freq[char] = 1
                    end += 1
                    length += 1
                elif (curr_char_freq[char] < p_freq[char]):
                    curr_char_freq[char] += 1
                    end += 1
                    length += 1
                else:
                    start_char = s[start]
                    curr_char_freq[start_char] -= 1
                    if curr_char_freq[start_char] == 0:
                        curr_char_freq.pop(start_char)
                    start += 1
                    length -= 1
            else:
                start = end + 1
                end += 1
                length = 0
                curr_char_freq = {char: 1}
            
            if length == len(p):
                output.append(start)
                
        return output
            
            