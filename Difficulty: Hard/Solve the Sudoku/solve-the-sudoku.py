import copy

class Solution:
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        
        # Your code here
        self.result = []
        self.sudoku(0, 0, mat)
        return self.result
        
    def check(self, row, col, mat, num):
        for column in range(0, 9):
            if mat[row][column] == num:
                return False
        
        for row_ in range(0, 9):
            if mat[row_][col] == num:
                return False
        
        sub_row, sub_col = row//3, col//3
        for row_ in range(0, 3):
            curr_row = row_ + sub_row * 3
            for col_ in range(0, 3):
                curr_col = col_ + sub_col * 3
                if mat[curr_row][curr_col] == num:
                    return False
        
        return True
                
        
        
    def sudoku(self, row, col, mat):
        if row == len(mat):
            self.result = copy.deepcopy(mat)
            return True
        if col == len(mat[0]):
            return self.sudoku(row+1, 0, mat)
        if mat[row][col] != 0:
            return self.sudoku(row, col+1, mat)
        for num in range(1, 10):
            if self.check(row, col, mat, num):
                mat[row][col] = num
                
                if self.sudoku(row, col+1, mat):
                    return True
                mat[row][col] = 0
        return False