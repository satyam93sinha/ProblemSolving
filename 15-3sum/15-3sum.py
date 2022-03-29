class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for index, num in enumerate(nums):
            # skipping the same num values to avoid duplicates
            if index != 0 and num == nums[index-1]:
                continue
            target = -num
            start, end = index + 1, len(nums) - 1
            while start < end:
                if nums[start] + nums[end] < target:
                    start += 1
                elif nums[start] + nums[end] > target:
                    end -= 1
                else:
                    answer.append([num, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while (start < end 
                           and (end == len(nums)-1
                           or nums[end] == nums[end + 1])):
                        end -= 1
        return answer