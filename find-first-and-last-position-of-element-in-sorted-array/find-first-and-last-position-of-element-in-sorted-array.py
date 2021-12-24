class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        first_occurence = self.first_occurence(nums, target)
        last_occurence = self.last_occurence(nums, target)
        return [first_occurence, last_occurence]
    

    def first_occurence(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        if start < len(nums) and nums[start] == target:
            return start
        else:
            return -1
    
    def last_occurence(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                start = mid + 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        if end > -1 and nums[end] == target:
            return end
        else:
            return -1
                