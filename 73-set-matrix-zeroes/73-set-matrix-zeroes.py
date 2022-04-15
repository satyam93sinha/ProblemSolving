class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                is_col = True
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        # set first row to zero
        if matrix[0][0] == 0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        
        # set first col to zero
        if is_col:
            for row in range(len(matrix)):
                matrix[row][0] = 0