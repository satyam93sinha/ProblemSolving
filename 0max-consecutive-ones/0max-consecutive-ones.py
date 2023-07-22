class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_ones = 0
        max_consecutive_ones = 0
        for num in nums:
            if num == 1:
                count_ones += 1
            else:
                count_ones = 0
            max_consecutive_ones = max(max_consecutive_ones, count_ones)
        
        return max_consecutive_ones