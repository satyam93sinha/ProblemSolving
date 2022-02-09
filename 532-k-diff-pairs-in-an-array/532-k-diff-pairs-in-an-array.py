"""
Edge Cases:
1. nums array is empty; not possible, a constraint
2. Sorted array;
"""

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        start, end = 0, 1
        count = 0
        while start < len(nums) and end < len(nums):
            if start > 0 and nums[start] == nums[start-1]:
                # same element, we have already computed for prev one,
                # so ignore this current
                start += 1
            elif start == end:
                # we can not consider start==end, so increment end
                end += 1
            elif nums[end]-nums[start] < k:
                # find a value greater than the present one, 
                # to increase the difference thus, increment end
                end += 1
            elif nums[end]-nums[start] > k:
                # find a val that gives less diff than current,
                # increment start
                start += 1
            else:
                # element is found, increment all start, end and count
                count += 1
                start += 1
                end += 1
        return count
        