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

3. Use two pointer
Intuition:
Sort the products array so that all the words are lexicographically aligned. Point left and right index at their correct position where the word starting with given char in searchWord could be found. Later, append the product to the result.
Time: O(n^2) -> len(searchWord) * len(products)
Space: O(len(answer)) if considering answer as extra space
"""

class Solution:
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        answer = []
        # sort products
        products.sort()
        # initialise left and right pointers
        left, right = 0, len(products) - 1
        # iterate over searchWord
        for index, char in enumerate(searchWord):
            # exclude all the words/product that doesn't start with
            # searchWord char
            # as products is sorted, we will get all the product
            # together at a place
            while (left <= right 
                   and (len(products[left]) <= index
                   or products[left][index] != char)):
                left += 1
            # shrinking the window size of word to consider in answer
            # left to right is the window where we can find answer
            # len(products[right]) <= index so that IndexError/out of bounds exception is not thrown
            while (left <= right
                  and (len(products[right]) <= index
                  or products[right][index] != char)):
                right -= 1
            # total length present or to consider
            # total number of words matching the prefix searchWord chars
            length = right - left + 1
            current_answer = []
            # if we simply append(left: left+3) it may append those products that do not have searchWord prefix so we need to append only those that are in range left to right and not more than 3
            for word_index in range(min(3, length)):
                current_answer.append(products[left + word_index])
            answer.append(current_answer)
        return answer
        