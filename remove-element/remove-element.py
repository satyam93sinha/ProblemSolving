"""
Test Cases:
[3,2,2,3]
3
[0,1,2,2,3,0,4,2]
2
[0,1,2,3]
4
[1]
1
[1,1,1,1,1]
1
[1,1,1,2]
1
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removal_element_index = 0
        for index, num in enumerate(nums):
            if num != val:
                nums[index], nums[removal_element_index] = nums[removal_element_index], nums[index]
                removal_element_index += 1
        return removal_element_index
        
        """
        same = 0
        for different, num in enumerate(nums):
            if nums[same] != val:
                same += 1
            elif num != val and nums[same] == val:
                nums[different], nums[same] = nums[same], nums[different]
                same += 1
        
        return same
        """
        
        """
        remove_element_index = 0
        for index, num in enumerate(nums):
            if num != val:
                nums[remove_element_index] = num
                remove_element_index += 1
        return remove_element_index
        """