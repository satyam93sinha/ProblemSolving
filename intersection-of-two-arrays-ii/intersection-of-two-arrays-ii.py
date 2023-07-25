# [1,2,2,1]
# [2,2]
# [4, 9, 5]
# [9, 4, 9, 8, 4]
# [1, 2, 3, 1, 2, 5]
# [5, 2, 3, 1, 2]
# [1, 1, 1]
# [1, 1, 1]
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = collections.Counter(nums1)
        nums2 = collections.Counter(nums2)
        answer = []
        for num in nums1:
            if num in nums2:
                answer.extend([num]*min(nums1[num], nums2[num]))
        return answer