class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_indices = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_indices.add((row, col))
        
        for row, col in zero_indices:
            for column in range(0, len(matrix[row])):
                matrix[row][column] = 0
            
            for row_index in range(0, len(matrix)):
                matrix[row_index][col] = 0
        