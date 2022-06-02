class Solution:
    def trap(self, height: List[int]) -> int:
        max_right = self.max_right(height.copy())
        max_left = self.max_left(height)
        print(max_right, max_left, height)
        for index in range(len(height)):
            water_trapped = min(max_right[index], max_left[index]) - height[index]
            height[index] = water_trapped
        return sum(height)
    
    def max_left(self, height: List[int]) -> List[int]:
        max_ = 0
        max_left = [0 for _ in range(len(height))]
        for index, height_ in enumerate(height):
            max_ = max(max_, height_)
            max_left[index] = max_
        
        return max_left
    
    def max_right(self, height: List[int]) -> List[int]:
        max_ = 0
        for index in range(len(height)-1, -1, -1):
            height_ = height[index]
            max_ = max(max_, height_)
            height[index] = max_
        
        return height