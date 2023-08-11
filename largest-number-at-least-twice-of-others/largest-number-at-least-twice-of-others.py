class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num, max_index, second_max = float('-inf'), -1, float('-inf')
        
        for index, num in enumerate(nums):
            if num >= max_num:
                second_max, max_num = max_num, num
                max_index = index
            
            elif num >= second_max:
                second_max = num
        
        if second_max*2 > max_num:
            return -1
        
        return max_index