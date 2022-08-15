class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = right = 0
        consecutive_ones = 0
        num_zeroes = 0
        
        while right < len(nums):
            # calculations
            if nums[right] == 0:
                num_zeroes += 1
            
            # slide the window
            # keep account of zeroes count
            while num_zeroes == 2:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1
            
            # ans <- calculations
            consecutive_ones = max(consecutive_ones, right - left + 1)
            right += 1
        return consecutive_ones