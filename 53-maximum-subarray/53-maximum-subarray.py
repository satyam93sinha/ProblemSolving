class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray_sum = float('-inf')
        current_sum = 0
        for num in nums:
            """
            current_sum += num
            if num > current_sum:
                current_sum = num
            """
            current_sum = max(current_sum + num, num)
            max_subarray_sum = max(max_subarray_sum, current_sum, num)
        
        return max_subarray_sum