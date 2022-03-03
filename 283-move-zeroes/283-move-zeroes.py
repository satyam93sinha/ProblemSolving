class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for index, num in enumerate(nums):
            if num != 0:
                nums[index], nums[zero] = nums[zero], nums[index]
                zero += 1