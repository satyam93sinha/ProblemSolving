class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hashmap = collections.defaultdict(set)
        col_hashmap = collections.defaultdict(set)
        matrix_hashmap = collections.defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if (board[row][col] in row_hashmap[row]
                   or board[row][col] in col_hashmap[col]
                   or board[row][col] in matrix_hashmap[(row//3, col//3)]):
                    return False
                row_hashmap[row].add(board[row][col])
                col_hashmap[col].add(board[row][col])
                matrix_hashmap[(row//3, col//3)].add(board[row][col])
        
        return True