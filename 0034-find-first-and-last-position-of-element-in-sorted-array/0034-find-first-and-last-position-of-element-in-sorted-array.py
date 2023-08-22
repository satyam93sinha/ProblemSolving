class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        starting_position = self.search_range_begin(nums, target)
        ending_position = self.search_range_end(nums, target)
        return [starting_position, ending_position]
    
    def search_range_begin(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
                res = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return res
    
    def search_range_end(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
                res = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return res