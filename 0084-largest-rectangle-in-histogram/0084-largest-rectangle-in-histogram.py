class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # calculate width and area
        next_smaller_left = self.next_smaller_left(heights)
        next_smaller_right = self.next_smaller_right(heights)
        print(next_smaller_left, next_smaller_right)
        max_area = -1
        
        for index in range(len(heights)):
            width = next_smaller_right[index] - next_smaller_left[index] - 1
            height = heights[index]
            area = width * height
            max_area = max(max_area, area)
        
        return max_area
        
        
    def next_smaller_left(self, heights: List[int]) -> List[int]:
        next_smaller_left = []
        stack = []
        
        for index, height in enumerate(heights):
            while stack and heights[stack[-1]]>= height:
                stack.pop()
            
            if stack:
                next_smaller_left.append(stack[-1])
            else:
                next_smaller_left.append(-1)
            
            stack.append(index)
        
        return next_smaller_left
    
    def next_smaller_right(self, heights: List[int]) -> List[int]:
        next_smaller_right = []
        stack = []
        
        for index in range(len(heights)-1, -1, -1):
            height = heights[index]
            while stack and heights[stack[-1]] >= height:
                stack.pop()
            
            if stack:
                next_smaller_right.append(stack[-1])
            else:
                next_smaller_right.append(len(heights))
            
            stack.append(index)
        
        next_smaller_right.reverse()
        
        return next_smaller_right
        
        