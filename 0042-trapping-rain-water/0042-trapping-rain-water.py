class Solution:
    def trap(self, height: List[int]) -> int:
        max_heights_left = self.max_heights_left(height)
        max_heights_right = self.max_heights_right(height)
        
        trap_rain_water = 0
        
        for index, height_ in enumerate(height):
            trap_rain_water += min(max_heights_left[index], max_heights_right[index]) - height_
        
        return trap_rain_water
    
    def max_heights_left(self, height: List[int]) -> List[int]:
        # find the max height for every element of height array towards its left
        max_left = 0
        max_heights_left_array = []
        
        for height_ in height:
            max_left = max(max_left, height_)
            max_heights_left_array.append(max_left)
        
        print("max left heights:", max_heights_left_array)
        return max_heights_left_array
    
    def max_heights_right(self, height: List[int]) -> List[int]:
        # find the max height for every element of height array towards its right
        max_right = 0
        max_heights_right_array = []
        
        for height_ in height[::-1]:
            max_right = max(max_right, height_)
            max_heights_right_array.append(max_right)
        
        max_heights_right_array.reverse()
        print("max right heights:", max_heights_right_array)
        return max_heights_right_array