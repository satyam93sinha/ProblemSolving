"""
Edge Cases:
1. Empty matrix; False
2. Single element in matrix; return target == element in matrix
3. Matrix of size mxn where number of rows and cols are not equal

Approaches:
1. Brute Force
Time: O(m*n) : Iterate over the matrix and compare every element
Space: O(1)

2. Use Binary Search (property matrix is sorted in some way)
Time: O(m + n)
Space: O(1)
Intuition:
Compare target with element in matrix and somehow reduce the search space and go in the direction of finding the target.
Algorithm: 
Ensure row and col does not go Out of Bounds
a) Initialise row, col = 0, len(matrix[0])-1  # start row and end of col
b) Compare target with matrix[row][col]
    i) decrement col -= 1 if target < matrix[row][col]
    ii) increment row += 1 if target > matrix[row][col]
    iii) if target == matrix[row][col] ; return True
c) If target is not found in the matrix ; return False
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0])-1
        
        # handling Out of Bounds
        while (0 <= row < len(matrix)
               and 0 <= col < len(matrix[0])):
            
            # target is found
            if target == matrix[row][col]:
                return True
            # target is smaller -> search in left area/go left
            elif target < matrix[row][col]:
                col -= 1
            # target is greater -> search in right area/go down or right
            else:
                row += 1
        
        # target not found in matrix
        return False