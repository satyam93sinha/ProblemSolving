class NSL:
    def nearest_small_left(self, array):
        stack = [] # to store [index, num]
        nsl = [0 for _ in range(len(array))]
        
        for index, num in enumerate(array):
            while stack and stack[-1][1] >= num:
                stack.pop()
            if stack:
                nsl[index] = stack[-1][0]
            else:
                nsl[index] = -1
            stack.append([index, num])
        
        return nsl

class NSR:
    def nearest_small_right(self, array):
        stack = [] # to store [index, num]
        nsr = [0 for _ in range(len(array))]
        length = len(array) - 1
        
        for index, num in enumerate(array[::-1]):
            while stack and stack[-1][1] >= num:
                stack.pop()
            if stack:
                nsr[length - index] = stack[-1][0]
            else:
                nsr[length - index] = len(array)
            stack.append([length-index, num])
        
        return nsr

class Area:
    def width(self, array):
        nsl = NSL().nearest_small_left(array)
        nsr = NSR().nearest_small_right(array)
        width = []
        
        for nsl_, nsr_ in zip(nsl, nsr):
            width.append(nsr_-nsl_-1)
        
        return width
    
    def area_of_array(self, array):
        width = self.width(array)
        area = []
        for index in range(len(width)):
            area.append(width[index] * array[index])
        
        return area

class MaxAreaHistogram:
    def max_area_histogram(self, array):
        area = Area().area_of_array(array)
        return max(area)



class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix = [[int(matrix[row][col]) for col in range(len(matrix[row]))] for row in range(len(matrix))]
        # print(matrix)
        max_area = float('-inf')
        current_histogram = [0 for _ in range(len(matrix[0]))]
        
        for row in matrix:
            for index, col in enumerate(row):
                if col == 1:
                    current_histogram[index] += col
                else:
                    current_histogram[index] = 0
            max_area = max(max_area,
                           MaxAreaHistogram().max_area_histogram(current_histogram))
        return max_area
        