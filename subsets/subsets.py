class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.power_set([], [], nums, 0)
    
    def power_set(self, output: List[List[int]], 
                  subset: List[int], 
                  nums: List[int], index: int) -> List[List[int]]:
        # base case
        if index >= len(nums):
            output.append(subset.copy())
            return output
        else:
            # include
            subset.append(nums[index])
            self.power_set(output, subset, nums, index + 1)
            subset.pop()
            
            # exclude
            self.power_set(output, subset, nums, index + 1)
            return output