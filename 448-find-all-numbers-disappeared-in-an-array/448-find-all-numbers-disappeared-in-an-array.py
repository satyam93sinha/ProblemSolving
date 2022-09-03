"""
Clarifying Questions:
1. Can nums array be empty?
2. Will the elements in nums array be both negative and positive or which one of them?
3. Can we somehow modify the array?

Edge Cases:
1. nums array is empty; not possible, a constraint
2. len(nums) == 1; check if the number present is 1, if not we return missing number as 1
3. len(nums) >= 2; check for missing numbers and return answer
    a) can contain duplicates
4. no num is missing from nums array

Test Cases:
Input -
[]
[2]
[1]
[1, 2, 3, 4]
[4, 2, 3, 1]
[1, 2, 3, 2]
[4, 3, 2, 7, 8, 2, 3, 1]

Output -
[]
[1]
[]
[]
[]
[4]
[5, 6]

Approaches:
1. Brute Force
Intuition:
Use additional space and data structure set
Time: O(n)
Space: O(n)

2. Optimized, use the information elements will be in range[1, n]
Intuition:
Steps -
1. Iterate over the nums array
2. for every num, generate a new_index = abs(num) - 1 and change the value's magnitude --> to negative which ensures this is visited and has already appeared in the array
3. we use abs(num) so that if we encounter any number that is already seen/visited/appeared converted to negative magnitude, we can compute its index(which is always positive).
Time: O(n), we visit every element once in the iteration
Space: O(1), we don't use any additional space
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            # compute new_index, index is always positive
            new_index = abs(num) - 1
            
            # change its magnitude
            if nums[new_index] > 0:
                nums[new_index] *= -1
            
        # 2nd pass to find the result, missing numbers
        for index, num in enumerate(nums, start=1):
            if num > 0:
                result.append(index)
        
        # return answer
        return result