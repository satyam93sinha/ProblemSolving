class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_freq = collections.Counter(nums2)
        output = []
        for num in nums1:
            if num in nums2_freq and nums2_freq[num] > 0:
                nums2_freq[num] -= 1
                output.append(num)
        
        return output