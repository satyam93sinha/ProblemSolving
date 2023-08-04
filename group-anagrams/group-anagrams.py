"""
Edge Cases:
    1. strs list can not be empty -- a constraint
    2. there is single word in the strs list -- should be an answer also
    3. there are distinct words in the strs list -- the strs list should be the answer
    4. all the words are anagrams of each other -- already an answer
    5. there are mixed words, some of them are anagrams of each other rest aren't -- GROUP ANAGRAMS

Test Cases:
    []
    ["abc"]
    [""]
    ["abc", "cde", "efg"]
    ["aba", "baa", "aab"]
    ["abc", "cba", "def", "ghi", "tea", "tan", "nat", "bat", "ate"]

Approaches:
    1. Brute Force
    Intuition:
        Iterate over the strs list and check if there are any other anagrams of it. 
        How to check for anagrams?
        Anagrams will have same frequency of all the characters in the word. Thus, we should check every word's character's frequency. While iterating, keep a dictionary/hashmap which stores this data for the word the outer for-loop iterates upon and keep generating the same for the word in inner for-loop. If they match, we keep them into one list within the resulting answer.
    Time Complexity: O(m*m*n) where m=len(strs), n=len(strs[i])
    Space Complexity: O(n) = O(26) = O(1) where n=len(strs[i]), we use dictionary/hashmap to store char frequency, as n is in range a-z as mentioned in the problem statement's constraint.
        
    2. Better Optimized
    Intuition:
        How can we solve it faster than O(m*m*n)?
        Why do we need outer and inner for-loop iteration? We can have hashmap, store every char frequency or generate a key somehow so that when we keep iterating over the strs[i] and directly match them with their anagrams. Let's build keys by sorting the strs[i], this way all the anagrams will look same/have same keys.
    Time Complexity: O(m*nlogn) where m=len(strs), n=len(strs[i])
    Space Complexity: O(m) if all the words of strs list are distinct, each of them will generate their individual keys.
    
    3. Optimized
    Intuition:
        Can we generate better keys, in less time complexity?
        We know that all the characters of strs will be lowercase english alphabets => a-z => 26 chars.
        So, thinking if it's possible to use this information somehow to generate the char-frequency of
        every word in strs, then we could use them as keys of hashmap.
    Time Complexity: O(m*n)
    Space Complexity: O(n) = O(26) = O(1)
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            # to build keys
            char_frequency = [0 for _ in range(26)]
            
            # building keys
            for char in word:
                char_frequency[ord(char) - ord('a')] += 1
            
            # as we have used a defaultdict, we already have this key and list(as value) present within the result defaultdict 
            result[tuple(char_frequency)].append(word)
        
        return result.values()   # result.values will return list of lists of values