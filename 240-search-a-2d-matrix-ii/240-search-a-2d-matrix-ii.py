"""
Edge Cases:
1. 1 x 1 matrix; there is only one element; if it is the target return true else false
2. empty matrix; return false bcoz no element can be found in empty matrix
3. matrix contain duplicate values even though it is sorted in ascending order; binary search can be used
4. not a square matrix; can contain only column/row; it won't matter until we handle IndexError
5. target is not present in matrix

Test Cases:
1. [[3]], target = 3, target = 5
2. [[]], target = 10
3. [[1, 2, 3, 4]], target = 3, target = 5
4. [[1], [2], [3]], target = 2, target = 6

Approaches:
1. Brute Force:
Intuition: check every element of matrix and compare with target, if found return True else False
Time: O(m*n)
Space: O(1)

2. Not Possible in this Question, use in Search a 2D Matrix :: Use Binary Search on every row to find if target exists
Time: O(m*log(n))
Space: O(1)

3. Not Possible bcoz rows and columns are sorted among themselves, next row may or may not be greater than previous row's last element :: Use Binary Search on rows to find the correct/possible row where target could be found and again use simple binary search to find the target in this row
Time: O(log(m) + log(n))
Space: O(1)

4. Start from last element of first row and compare with target, if target is greater than this element we have to search in next row else decrement column to search for its correct location.
Time: O(m + n)
Space: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_start, row_end = 0, len(matrix)-1
        col_start, col_end = 0, len(matrix[0])-1
        while row_start <= row_end and col_end >= col_start:
            if target > matrix[row_start][col_end]:
                row_start += 1
            elif target < matrix[row_start][col_end]:
                col_end -= 1
            else:
                return True
        
        return False