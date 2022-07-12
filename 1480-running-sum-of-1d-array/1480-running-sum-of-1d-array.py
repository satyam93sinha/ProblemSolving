"""
#### Edge Cases:
1. nums is empty; return [] -> not possible, a constraint
2. len(nums) == 1; return nums
3. len(nums) >= 2; calculate running sum and return the answer.
Here, answer can be a new array or if allowed, we can modify the nums array

#### Test Cases:
[1]
[1, 2]
[3, 8, 1]

#### Approaches:
1. Brute Force
Intuition:
Two nested loops, the inner loop calculates the sum until outer loop's index
and builds the answer, we need a new answer array for this.
Time: O(n^2)
Space: O(n) for answer

2. Prefix Sum
Intuition:
Simply sum previous and current elements of the array and return it as the answer.
Time: O(n)
Space: O(1) if using nums else O(n) for answer array
"""



class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for index in range(1, len(nums)):
            nums[index] = nums[index - 1] + nums[index]
        
        return nums