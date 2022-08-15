class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = heights.copy()
        expected.sort()
        different_indices = 0
        for height, expect in zip(heights, expected):
            if height != expect:
                different_indices += 1
        
        return different_indices