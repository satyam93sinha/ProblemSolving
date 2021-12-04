class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        histogram = [0 for _ in range(cols)]
        max_area_matrix = 0
        for row in range(rows):
            for col in range(cols):
                matrix_element = int(matrix[row][col])
                if matrix_element == 1:
                    histogram[col] += matrix_element
                else:
                    histogram[col] = 0
            max_area_matrix = max(max_area_matrix,
                                  MaxAreaHistogram().max_area_histogram(histogram))
        return max_area_matrix
                    
        

        
class MaxAreaHistogram:
    def max_area_histogram(self, array: List[int]) -> int:
        left = NearestSmallerLeft().nearest_smaller_left(array)
        right = NearestSmallerRight().nearest_smaller_right(array)
        # calculate width
        width = [right[index]-left[index]-1 for index in range(len(array))]
        
        # calculate max_area and return max_area
        max_area = 0
        for index in range(len(array)):
            max_area = max(max_area, width[index]*array[index])
        return max_area

class NearestSmallerLeft:
    def nearest_smaller_left(self, array: List[int]) -> List[int]:
        stack = []
        left = [0 for _ in range(len(array))]
        for index in range(len(array)):
            while stack and array[stack[-1]] >= array[index]:
                stack.pop()
            if stack:
                left[index] = stack[-1]
            else:
                left[index] = -1
            stack.append(index)
        return left

    
class NearestSmallerRight:
    def nearest_smaller_right(self, array: List[int]) -> List[int]:
        stack = []
        right = [0 for _ in range(len(array))]
        for index in range(len(array)-1, -1, -1):
            while stack and array[stack[-1]] >= array[index]:
                stack.pop()
            if stack:
                right[index] = stack[-1]
            else:
                right[index] = len(array)
            stack.append(index)
        return right