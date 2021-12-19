class NumFreq:
    def __init__(self, num, frequency):
        self.num = num
        self.frequency = frequency
    
    def __lt__(self, other):
        if self.frequency < other.frequency:
            return True
        else:
            if self.frequency == other.frequency:
                return self.num > other.num
            else:
                return False

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dictionary = collections.Counter(nums)
        to_sort = []
        for key, val in dictionary.items():
            to_sort.append(NumFreq(key, val))
        
        sorted_list = sorted(to_sort)
        
        result = []
        for element in sorted_list:
            for freq in range(element.frequency):
                result.append(element.num)
        
        return result