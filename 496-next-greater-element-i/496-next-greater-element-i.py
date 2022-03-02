class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        element_index_dict, next_greater_nums2 = self.next_greater(nums2)
        output = []
        for num in nums1:
            next_greater = next_greater_nums2[element_index_dict[num]]
            output.append(next_greater)
        return output
    
    def next_greater(self, nums: List[int]) -> (Dict, List[int]):
        stack = []
        element_index_dict = {}
        next_greater_element = [0 for _ in range(len(nums))]
        for index in range(len(nums)-1, -1, -1):
            # stores element and its index in dictionary
            element_index_dict[nums[index]] = index
            while stack and stack[-1] < nums[index]:
                stack.pop()
            if not stack:
                next_greater_element[index] = -1
            else:
                next_greater_element[index] = stack[-1]
            stack.append(nums[index])
        
        return element_index_dict, next_greater_element