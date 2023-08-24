class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float('-inf'))
        left, right = 0, len(nums)-2
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            elif nums[mid-1] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1