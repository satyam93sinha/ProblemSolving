class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for index, num in enumerate(nums):
            if index != 0 and num == nums[index-1]:
                # skipping the first number as duplicate candidate
                continue
            
            j = index + 1
            k = len(nums)-1
            while j < k:
                if nums[j] + nums[k] + num == 0:
                    triplets.append([num, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # skip second and third duplicate candidates
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[j] + nums[k] + num > 0:
                    k -= 1
                else:
                    j += 1
        
        return triplets