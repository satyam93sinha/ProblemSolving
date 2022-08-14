"""
Edge Cases:
1. Array does not contain any duplicate element; return length of the array
2. Array is empty; return length of array or zero
3. Array contains duplicate elements; reorder them and return the length of array which contains only single elements, no duplicates
4. Array contains only duplicates

Test Cases:
1. [1, 2, 3, 4, 5]
2. []
3. [1, 1, 1, 2, 3, 3]
4. [1, 1, 1, 1, 1]

Approaches:
1. Brute Force
Intuition:
Create a new array and append only unique elements skip the duplicates. How can we skip the duplicates?
Ans-> We know that given array is sorted so we could append the 0th index element into new array then iterate over given array and append only those elements that do not match with previous/last element of new array.
Time: O(n) iterate over given array
Space: O(n) extra array

2. Two pointer
Intuition:
Maintain seen and unseen pointers to track index element which has to be overwritten and iterator variable respectively. Index right before seen or unseen variables would contain the character or letters already encountered so while iterating over the array, moving unseen variable gives an insight of which to be included and which not.
Time: O(n)
Space: O(1) in-place, no extra space will be used
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case if nums has zero or single element
        if len(nums) < 2:
            return len(nums)
        
        # Edge case, nums has more than one element, could or couldn't contain duplicates
        seen = 1
        for unseen in range(1, len(nums)):
            if nums[unseen] != nums[seen - 1]:
                nums[seen] = nums[unseen]
                seen += 1
        
        return seen
        
        """
        start = 1
        for end in range(1, len(nums)):
            if nums[end] != nums[end-1]:
                nums[start] = nums[end]
                start += 1
        return start
        """
        
        """
        seen = 1
        for unseen in range(1, len(nums)):
            if nums[unseen] != nums[seen-1]:
                nums[seen] = nums[unseen]
                seen += 1
        return seen
        """