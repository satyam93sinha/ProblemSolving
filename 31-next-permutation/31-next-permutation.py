class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        # finding the first decrementing element,
        # it encounters index 0 iff nums is in decreasing order
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return
        i -= 1
        # finding just larger element than the one at index i
        while nums[i] >= nums[j]:
            # print(f"i:{i}, j:{j}")
            j -= 1
        
        # swap
        nums[i], nums[j] = nums[j], nums[i]
        
        start, end = i+1, len(nums)-1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        