class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        new_matrix = [0 for _ in range(len(matrix[0]))]
        max_area = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] != "0":
                    new_matrix[col] += int(matrix[row][col])
                else:
                    new_matrix[col] = 0

            max_rectangle_area = MaxRectangleArea()
            current_area = max_rectangle_area.largestRectangleArea(new_matrix)
            max_area = max(max_area, current_area)
        
        return max_area

class MaxRectangleArea:
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
        
        