class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}
        for string in strs:
            string_sorted = self.sort_string(string)
            if string_sorted in anagrams_dict:
                anagrams_dict[string_sorted].append(string)
            else:
                anagrams_dict[string_sorted] = [string]
        
        answer = []
        for key, val in anagrams_dict.items():
            answer.append(val)
        
        return answer
    
    def sort_string(self, string: str) -> str:
        return ''.join(sorted(string))