class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = collections.Counter(nums1)
        nums2 = collections.Counter(nums2)
        answer = []
        for num in nums1:
            if num in nums2:
                answer.extend([num]*min(nums1[num], nums2[num]))
        return answer