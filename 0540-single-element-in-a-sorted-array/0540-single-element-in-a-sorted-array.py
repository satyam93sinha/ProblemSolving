class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        if left == right:
            return nums[0]
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] != nums[mid-1] and nums[mid] != nums[(mid+1)%len(nums)]:
                return nums[mid]
            
            elif nums[mid] == nums[mid-1]:
                if (mid-0+1)%2 == 1:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if (mid+1-0)%2 == 1:
                    left = mid + 1
                else:
                    right = mid - 1