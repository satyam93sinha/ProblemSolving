class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            if index > 0:
                nums[index] += nums[index-1]
        return nums