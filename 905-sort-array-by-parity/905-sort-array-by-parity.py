class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        insert_even = 0
        for index, num in enumerate(nums):
            if num % 2 == 0:
                nums[insert_even], nums[index] = nums[index], nums[insert_even]
                insert_even += 1
        
        return nums