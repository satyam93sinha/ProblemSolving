"""
Edge Cases:
1. Empty matrix; not possible, a constraint
2. len(matrix) == 1, rows=1, cols=1 so 1x1 matrix
3. rows = 2, cols = 1 so cols < rows
4. rows = 1, cols = 4 so rows < cols => Maximum Area Histogram
5. all the elements are 0s => MAH = 0
6. all the elements of the matrix are 1, MAH = 1

Test Cases:
[[]]
[["0"]]
[["1"]]
[["1"], ["0"]]
[["1"], ["1"]]
[["1", "0", "0", "1"]]
[["1", "1", "1", "1"]]

Approaches:
1. Brute Force/Using Nearest Smallest to Left and Nearest Smallest to Right
Intuition:
We have already solved Maximum Area Histogram and know the way to solve it. Similarities, we have to calculate the maximum area of histogram in both the cases with single difference of 2D and 1D arrays. 

Is it possible to break this 2D array down to 1D array and solve for Maximum Area Histogram?
Yes, consider/take first row as new array for which we have to fetch/calculate maximum area histogram. Thereafter, we keep adding the elements from other rows to this new array building more histograms(big or small depends upon 1s and 0s). If the element to be added to the new array is 1, we simply add it else we make the new array column to 0.
Time: O(rows x columns)
Space: O(columns) because we are creating a new array building histogram of single row(1D array) and len(columns) columns
"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        histogram = [int(bin_num) for bin_num in matrix[0]]
        max_area = self.histogram_area(histogram)
        rows, cols = len(matrix), len(matrix[0])
        for row in range(1, rows):
            for col in range(cols):
                if matrix[row][col] != "0":
                    histogram[col] += int(matrix[row][col])
                else:
                    histogram[col] = 0  # base is 0, can't form a histogram so making it 0
        
            current_max_area = self.histogram_area(histogram)
            max_area = max(max_area, current_max_area)

        return max_area
    
    def histogram_area(self, histogram: List[int]) -> int:
        width = self.width_of_histograms(histogram)
        max_area = 0
        for width_, height_ in zip(width, histogram):
            max_area = max(width_*height_, max_area)
        
        return max_area
    
    def width_of_histograms(self, histogram: List[int]) -> List[int]:
        nearest_smallest_left = self.nearest_smallest_left(histogram)
        nearest_smallest_right = self.nearest_smallest_right(histogram)
        
        width = [right-left-1 for left, right in zip(nearest_smallest_left, nearest_smallest_right)]
        
        return width
    
    def nearest_smallest_left(self, histogram: List[int]) -> List[int]:
        stack = []
        nsl_index = [0 for _ in range(len(histogram))]
        for index, num in enumerate(histogram):
            while stack and stack[-1][0] >= num:
                stack.pop()
            if not stack:
                nsl_index[index] = -1
            else:
                nsl_index[index] = stack[-1][1]
            stack.append([histogram[index], index])
        
        return nsl_index
    
    def nearest_smallest_right(self, histogram: List[int]) -> List[int]:
        stack = []
        nsr_index = [0 for _ in range(len(histogram))]
        for index in range(len(histogram)-1, -1, -1):
            num = histogram[index]
            while stack and stack[-1][0] >= num:
                stack.pop()
            
            if not stack:
                nsr_index[index] = len(histogram)
            else:
                nsr_index[index] = stack[-1][1]
            stack.append([histogram[index], index])
        return nsr_index