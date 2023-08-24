class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] <= nums[mid-1] and nums[mid] <= nums[(mid+1)%len(nums)]:
                return nums[mid]
            
            elif nums[left] <= nums[mid]:
                if nums[mid] <= nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right = mid - 1