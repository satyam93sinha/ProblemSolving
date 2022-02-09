class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index, nums2_index = m-1, n-1
        index = len(nums1)-1
        while nums1_index > -1 and nums2_index > -1:
            if nums1[nums1_index] > nums2[nums2_index]:
                nums1[index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[index] = nums2[nums2_index]
                nums2_index -= 1
            index -= 1
        
        while nums1_index > -1:
            nums1[index] = nums1[nums1_index]
            nums1_index -= 1
            index -= 1
        
        while nums2_index > -1:
            nums1[index] = nums2[nums2_index]
            nums2_index -= 1
            index -= 1