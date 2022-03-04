class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary_diagonal = 0
        rows, cols = len(mat), len(mat[0])
        row, col = 0, 0
        while row < rows and col < cols:
            primary_diagonal += mat[row][col]
            row += 1
            col += 1
        
        secondary_diagonal = 0
        row, col = 0, cols-1
        while row < rows and col > -1:
            secondary_diagonal += mat[row][col]
            row += 1
            col -= 1
        
        if len(mat) % 2 == 1:
            secondary_diagonal -= mat[len(mat)//2][len(mat[0])//2]
        
        return primary_diagonal + secondary_diagonal