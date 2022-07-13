class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums)-1
        sorted_index = len(nums)-1
        answer = [0 for _ in range(len(nums))]
        
        while start <= end:
            start_pow, end_pow = pow(nums[start], 2), pow(nums[end], 2)
            if start_pow < end_pow:
                answer[sorted_index] = end_pow
                end -= 1
            else:
                answer[sorted_index] = start_pow
                start += 1
            sorted_index -= 1
        return answer