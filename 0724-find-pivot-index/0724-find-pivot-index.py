class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for index, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return index
            left_sum += num
        
        return -1