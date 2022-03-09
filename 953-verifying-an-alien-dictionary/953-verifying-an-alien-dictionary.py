class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_index_dict = {char: index for index, char in enumerate(order)}
        for index in range(len(words)-1):
            word1, word2 = words[index], words[index+1]
            for index1, char1 in enumerate(word1):
                # word2 is shorter than word1
                if index1 == len(word2):
                    return False
                # char are different
                if word1[index1] != word2[index1]:
                    if (char_index_dict[word1[index1]] > char_index_dict[word2[index1]]):
                            return False
                    break
        
        return True