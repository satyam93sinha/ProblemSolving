#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.ROWS = self.COLS = self.n = n
        self.result = []
        self.row_set = set()
        
        return self.helper(col=0, output=[])
    
    def helper(self, col, output=[]):
        if col == self.COLS:
            self.result.append(output.copy())
            return self.result
        
        for row in range(self.ROWS):
            if self.check(row, col):
                self.board[row][col] = 1
                output.append(row+1)
                self.row_set.add(row)
                
                self.helper(col+1, output)
                
                self.board[row][col] = 0
                output.pop()
                self.row_set.discard(row)
        
        return self.result
    
    def check(self, row, col):
        if row in self.row_set:
            return False
        
        for i in range(1, self.n):
            if row-i >= 0 and col-i >= 0:
                if self.board[row-i][col-i] == 1:
                    return False
            
            if row+i < self.ROWS and col-i >= 0:
                if self.board[row+i][col-i] == 1:
                    return False
        
        return True
                