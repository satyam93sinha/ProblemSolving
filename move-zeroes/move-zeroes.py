class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for non_zero_index, num in enumerate(nums):
            if num != 0:
                nums[zero_index], nums[non_zero_index] = num, nums[zero_index]
                zero_index += 1
        
        return zero_index