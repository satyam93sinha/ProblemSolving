"""
Edge Cases:
1. Matrix of 1x1 ; check if element is present and return True or False
2. Matrix of mxn ; find the row that has/may have target element and apply binary search to reduce the time complexity to O(m + logn)
3. Empty matrix ; return False
4. row and col should not go beyond array's indices

Approaches:
1. Brute Force
Time: O(m x n), search every element of matrix for target
Space: O(1)

2. Use Binary + Linear Search
Time: O(m + n), ignore the search space/row which can not contain the target by checking if target is in range of row's start column value and row's end column value. If it is not, change the row. When row is found, check every element of row for target
Space: O(1)

3. Use Binary + Linear Search
Time: O(m + logn), find the row that may contain target and apply binary search to find the target (use property array is sorted row-wise, column-wise and last column to first column of next row)
Space: O(1)

4. Use Binary Search
Time: O(logm + logn), first search for correct row(use property columns are sorted and elements are also sorted in matrix) then, search for element in row found using simple binary search, on columns.
Space: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Approach4: Time-O(logm + logn), Space: O(1)
        row_start, row_end = 0, len(matrix)-1
        while row_start <= row_end:
            # find mid
            mid_row = (row_start + row_end) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                return self.binary_search(matrix[mid_row], target)
            elif matrix[mid_row][0] > target:
                row_end = mid_row - 1
            else:
                row_start = mid_row + 1
        return False
        
        
        
        
        
        
        """
        row_start, row_end = 0, len(matrix)-1
        while row_start <= row_end:
            mid_row = (row_start + row_end) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                # we found row containing target, search in this row/array
                return self.binary_search(matrix[mid_row], target)
            elif target < matrix[mid_row][0]:
                # target is less than first element of matrix[mid_row]
                row_end = mid_row - 1
            else:
                # target is greater than last element of matrix[mid_row]
                row_start = mid_row + 1
        # target not found, row_start > row_end
        return False
        """
        
        """
        # Approach3: Time: O(m + logn)
        row, col = 0, len(matrix[0])-1
        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
            if matrix[row][0] <= target <= matrix[row][col]:
                return self.binary_search(matrix[row], target)
            elif target > matrix[row][col]:
                row += 1
            else:
                break
        return False
        """
        
    def binary_search(self, array, target):
        left, right = 0, len(array)-1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return True
            elif target < array[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
