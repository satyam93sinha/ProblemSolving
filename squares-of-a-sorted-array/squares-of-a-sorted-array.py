class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums)-1
        sorted_squares_list = [0 for _ in range(len(nums))]
        insertion_index = len(sorted_squares_list) - 1
        while start <= end:
            if abs(nums[start]) > abs(nums[end]):
                sorted_squares_list[insertion_index] = pow(nums[start], 2)
                start += 1
            else:
                sorted_squares_list[insertion_index] = pow(nums[end], 2)
                end -= 1
            
            insertion_index -= 1
        
        return sorted_squares_list