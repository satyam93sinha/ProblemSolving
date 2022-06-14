class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater_elements = {}
        for index in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] < nums2[index]:
                stack.pop()
            greater_elements[nums2[index]] = stack[-1] if stack else -1
            stack.append(nums2[index])
        
        answer = [greater_elements[num] for num in nums1]
        
        return answer