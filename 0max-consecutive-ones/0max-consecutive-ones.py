class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_ones = 0
        max_consecutive_ones = 0
        for num in nums:
            if num == 1:
                current_ones += 1
            else:
                current_ones = 0
            
            max_consecutive_ones = max(max_consecutive_ones, current_ones)
        
        return max_consecutive_ones