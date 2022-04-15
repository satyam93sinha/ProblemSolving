class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_row_indices = set()
        zero_col_indices = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_row_indices.add(row)
                    zero_col_indices.add(col)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zero_row_indices or col in zero_col_indices:
                    matrix[row][col] = 0
        