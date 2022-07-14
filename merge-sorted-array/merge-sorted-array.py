class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:  # or n <= 0
            return nums1
        fill_index = m + n - 1
        m, n = m-1, n-1
        
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[fill_index] = nums1[m]
                m -= 1
            else:
                nums1[fill_index] = nums2[n]
                n -= 1
            fill_index -= 1

        while n >= 0:
            nums1[fill_index] = nums2[n]
            n -= 1
            fill_index -= 1
        