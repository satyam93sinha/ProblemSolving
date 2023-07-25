class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list2 = {word: index for index, word in enumerate(list2)}
        min_sum = 2000
        
        common_words_least_index_sum = []
        for index, word in enumerate(list1):
            if word in list2:
                curr_sum = index + list2[word]
                if curr_sum == min_sum:
                    common_words_least_index_sum.append(word)
                elif curr_sum < min_sum:
                    common_words_least_index_sum = [word]
                    min_sum = curr_sum
        
        return common_words_least_index_sum