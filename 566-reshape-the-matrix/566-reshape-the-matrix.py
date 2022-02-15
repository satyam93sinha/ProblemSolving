"""
Edge Cases:
1. rxc exceeds/is less than mxn; no new matrix can be created bcoz it won't accomodate all the elements of mxn original matrix
2. When rxc can accomodate all the elements of the original matrix

Approaches:
1. Brute Force
Intuition:
Create a result matrix of rxc and as we iterate through the elements of the original array we keep pushing them to the result array and updating the row and col.
Time: O(mxn) == O(rxc)
Space: O(mxn) == O(rxc)
"""

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n == r*c:
            result = [[-1001 for _ in range(c)] for _ in range(r)]
            row, col = 0, 0
            for m_row in range(m):
                for n_col in range(n):
                    if row < r and col < c:
                        result[row][col] = mat[m_row][n_col]
                        col += 1
                    if row < r and col == c:
                        row += 1
                        col = 0
                    
            return result
        
        else:
            return mat
        