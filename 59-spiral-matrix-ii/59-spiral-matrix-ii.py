class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        value = 1
        rows = cols = n
        left, right, top, bottom = 0, cols-1, 0, rows-1
        output = [[0 for _ in range(cols)] for _ in range(rows)]
        
        while left <= right and top <= bottom:
            # go from left -> right on top row
            for left_right_index in range(left, right+1):
                output[top][left_right_index] = value
                value += 1
            
            # increase top
            top += 1
            # go from top -> bottom on right col
            for top_bottom_index in range(top, bottom+1):
                output[top_bottom_index][right] = value
                value += 1
            
            # decrement right
            right -= 1
            # go from right -> left on bottom row
            for right_left_index in range(right, left-1, -1):
                output[bottom][right_left_index] = value
                value += 1
            
            # decrement bottom
            bottom -= 1
            # go from bottom -> top on left col
            for bottom_top_index in range(bottom, top-1, -1):
                output[bottom_top_index][left] = value
                value += 1
            
            # increment left
            left += 1
        
        return output