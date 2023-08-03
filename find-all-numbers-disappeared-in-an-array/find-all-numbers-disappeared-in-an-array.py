class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # iterate over num in nums, consider this num as index
        # mark those num_indices as negative/visited
        for num in nums:
            num_index = abs(num) - 1
            
            if nums[num_index] > 0:
                nums[num_index] *= -1
            
        result = []
        for index, num in enumerate(nums, start=1):
            if num > 0:
                result.append(index)
        
        return result