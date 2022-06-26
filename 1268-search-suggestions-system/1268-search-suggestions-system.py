"""
Edge Cases:
1. products is empty, searchWord is present; return [[]], no suggestion possible, a constraint so this edge case is not possible
2. at least one product is present for the given searchWord; return the list of all possible products that begins with characters typed in searchWord

Approaches:
1. Brute Force
Intuition:
Keep all the products in a list(already present), search for the words or product which begins with the char as typed in the searchWord and append it to the answer list, return this answer.
Time: O(len(products) * len(word) * len(searchWord))
Space: O(len(answer))

2. Use Trie
Intuition:
Design a trie and then check if the char present in searchWord returns true when checked for startsWith. If true, crawl level by level in trie and append the whole word to answer, this will run three times because we need at most three such words/products in every answer
Time: O(len(searchWord) * len(word))
Space: O(26*n) => O(1)
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
        for char in word:
            index = self.char_to_index(char)
            if not crawl.children[index]:
                crawl.children[index] = self.create_trie_node()
            crawl = crawl.children[index]
        crawl.end_of_word = True
    
    def starts_with(self, prefix: str) -> bool:
        crawl = self.root
        for char in prefix:
            index = self.char_to_index(char)
            if not crawl.children[index]:
                return None
            crawl = crawl.children[index]
        return crawl
    
    def get_words_starting_with(self, prefix: str) -> List[str]:
        crawl = self.starts_with(prefix)
        if crawl:
            result = self.dfs_with_prefix(crawl, prefix, [])
            return result
    
    def dfs_with_prefix(self, crawl, word, result):
        if len(result) == 3:
            return result
        if crawl.end_of_word:
            result.append(word)
        
        # dfs on all possible paths
        for index in range(26):
            char = chr(ord('a') + index)
            if crawl.children[index]:
                self.dfs_with_prefix(crawl.children[index], word+char, result)
        
        return result
    

class Solution:
    def __init__(self):
        self.trie_ds = Trie()
    
    def build_trie(self, products: List[str]) -> None:
        for product in products:
            self.trie_ds.insert(product)
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # build trie data structure
        self.build_trie(products)
        
        # check for starts_with for every char sequence of searchWord
        answer = []
        prefix = ''
        for char in searchWord:
            prefix += char
            answer.append(self.trie_ds.get_words_starting_with(prefix))
        return answer