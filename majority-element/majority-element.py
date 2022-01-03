from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_frequency = Counter(nums)
        max_frequency = nums[0]
        for num, freq in nums_frequency.items():
            if nums_frequency[max_frequency] < freq:
                max_frequency = num
        
        return max_frequency