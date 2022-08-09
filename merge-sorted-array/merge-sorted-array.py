"""
PREREQUISITES:
Both the arrays are already sorted among themselves.
EDGE CASES:
Both the arrays are empty; do nothing
One of the array is empty, fill nums1 if num2 is empty and/else return. nums1 contains the answer.
nums1 has all the elements lesser than nums2 or vice versa; store them at correct places in nums1 and return
numbers/elements present in nums1 and/or nums2 have negative values

TEST CASES:
nums1 = [], nums2 = []
[1, 2, 3] []
[0, 0] [1, 2]
[1, 2, 3, 0, 0] [4, 5]
[4, 5, 6, 0, 0] [1, 2]
[-1, -2, 0, 0] [2, -5]

APPROACHES:
Brute Force
Intuition:
Place all the elements from nums2 into nums1 and sort nums1.
Time: O(nlogn) for sorting
Space: O(1) no extra space used for sorting

Optimized
Intuition:
index nums1_index, nums2_index to their last elements
compare these two elements and whichever is greater place that in ans_index. Here, ans_index will be len(nums1) - 1
keep decrementing nums1_index and nums2_index based on point-2 and ans_index after filling it in every iteration
Time: O(m + n)
Space: O(1)

"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index, nums2_index = m-1, n-1
        ans_index = m + n - 1
        
        while nums1_index >= 0 and nums2_index >= 0:
            if nums1[nums1_index] > nums2[nums2_index]:
                nums1[ans_index] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[ans_index] = nums2[nums2_index]
                nums2_index -= 1
            ans_index -= 1
        
        # remaining elements from nums2
        while nums2_index >= 0:
            nums1[ans_index] = nums2[nums2_index]
            nums2_index -= 1
            ans_index -= 1
        
        