"""
Deduction:
1. nums array is sorted in ascending order
2. place the result in first half of the array and return the length of array until the placed elements
3. do not allocate extra space, modify in-place

To Do: remvoe some duplicates in-place such that unique element appears at most twice(unique element can either appear once or twice but not more than that)

Edge Cases:
1. Brute Force
Time: O(n)
Space: O(n) for extra space to store the result
Intuition:
Keep a dictionary containing num and their frequency. Iterate through nums array and if the frequency of the element in nums is equal to or greater than 2, we append it twice else if it's unique, we append it only once. This way we will have result array containing the answer.

2. Pop unwanted elements
Time: O(n^2)
Space: O(1)

3. Use Two Pointer Approach
Time: O(n)
Space: O(1)
Intuition:
Maintain a pointer marking overwriting_position/swap_position which will be changed/replaced by the other iterator element.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        position, count = 1, 1
        for iterator in range(1, len(nums)):
            if nums[iterator] == nums[iterator-1]:
                # prev and curr elements are same so increment count
                count += 1
            else:
                # prev and curr elements are different so reset count
                count = 1
            
            # for count<=2, position can be incremented after overwriting
            if count <= 2:
                nums[position] = nums[iterator]
                position += 1
        
        return position