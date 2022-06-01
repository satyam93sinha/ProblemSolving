class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [0 for _ in range(len(nums))]
        sum_ = 0
        for index, num in enumerate(nums):
            sum_ += num
            running_sum[index] = sum_
        
        return running_sum