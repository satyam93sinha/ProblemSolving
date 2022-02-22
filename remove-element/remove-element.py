class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        remove_element_index = 0
        for index, num in enumerate(nums):
            if num != val:
                nums[remove_element_index] = num
                remove_element_index += 1
        return remove_element_index