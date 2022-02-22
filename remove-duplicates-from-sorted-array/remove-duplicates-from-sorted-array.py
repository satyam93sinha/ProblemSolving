"""
Test Cases:
[1,1,2]
[0,0,1,1,1,2,2,3,3,4]
[1,2,3,4,5]
[1]
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_ptr = 0
        for curr in range(len(nums)):
            if nums[unique_ptr] != nums[curr]:
                unique_ptr += 1
                nums[unique_ptr] = nums[curr]
        return unique_ptr + 1