class Solution:
    def trap(self, height: List[int]) -> int:
        # Edge case
        if len(height) < 3:
            return 0
        
        # Time: O(n), Space: O(1) using two pointer approach
        # for explanation check Tech Dose youtube video
        max_left = max_right = 0
        left, right = 0, len(height) - 1
        trapped_water = 0
        while left < right:
            # go from left to right
            if height[left] <= height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    water_level = max_left
                    trapped_water += (water_level - height[left]) * 1
                left += 1
			# go from right to left
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    water_level = max_right
                    trapped_water += (water_level - height[right]) * 1
                right -= 1
        
        return trapped_water