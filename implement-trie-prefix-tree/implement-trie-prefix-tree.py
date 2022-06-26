"""
Edge Cases:
1. No word is inserted but it is searched or checked for startsWith; return False
2. Single word is inserted, search and startsWith returns True if found
3. For search, ensure we check end_of_word is True. startsWith doesn't require end_of_word to be True

Approaches:
1. Brute Force
Intuition:
Dictionary provides O(1) time insertion and search so insert word to a dictionary. For startsWith, we need to check all the words in dictionary and return True if any word starts with given prefix, time taken would be O(len(dictionary) * len(words))
Time: O(len(dictionary) * len(word))
Space: O(len(dictionary)) == O(n), we are not reusing the already inserted characters as we would do in Trie data structure

2. Use Trie Data Structure
Intuition:
Keep a TrieNode containing children and end_of_word as instance objects. Whenever a word is inserted we crawl the children and insert characters, later mark end_of_word as True differentiating it from those which haven't been inserted.
Time: O(len(longest word))
Space: O(26*n), where n is total number of words
"""

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = self.create_trie_node()
    
    def create_trie_node(self):
        return TrieNode()
    
    def char_to_index(self, char: str) -> int:
        return ord(char) - ord('a')

    def insert(self, word: str) -> None:
        crawl = self.root
        # level would be marked by length of word, we can also do this level for loop as
        # for char in word: -> the level would be len(word) in all the cases
        for level in range(len(word)):
            # get the index where we need to crawl or insert char
            index = self.char_to_index(word[level])
            # if this char is not present in the trie level -> children
            if not crawl.children[index]:
                crawl.children[index] = self.create_trie_node()
            # char is present in the trie data structure
            # move/crawl to the next level
            crawl = crawl.children[index]
        # mark end_of_word
        crawl.end_of_word = True

    def search(self, word: str) -> bool:
        crawl = self.root
        # crawl level by level until word's length is reached
        # or crawl over every char of the word
        for char in word:
            # get the index where this char could be present in trie's children
            index = self.char_to_index(char)
            # if index is None, char is not present in trie, return False
            if not crawl.children[index]:
                return False
            # crawl/traverse to another level in search of the char
            crawl = crawl.children[index]
        # check if we have traversed/crawled to the end of word
        # if true return true else false
        return crawl.end_of_word

    def startsWith(self, prefix: str) -> bool:
        crawl = self.root
        # crawl over every char of the word
        for char in prefix:
            # find the place/index current char can be placed
            index = self.char_to_index(char)
            # if char is not present, the prefix can not be present so return False
            if not crawl.children[index]:
                return False
            # crawl/traverse to another level
            crawl = crawl.children[index]
        # we have traversed the whole prefix which means we found the prefix
        # return True
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)