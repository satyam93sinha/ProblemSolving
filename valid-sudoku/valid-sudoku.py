class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        sub_box_dict = defaultdict(set)
        
        for row in range(9):
            row_set = set()
            col_set = set()
            for col in range(9):
                # row
                if board[row][col] != ".":
                    if board[row][col] in row_set:
                        return False
                    else:
                        row_set.add(board[row][col])
                    
                    if board[row][col] in sub_box_dict[(row//3, col//3)]:
                        return False
                    else:
                        sub_box_dict[(row//3, col//3)].add(board[row][col])
                
                # col
                if board[col][row] != ".":
                    if board[col][row] in col_set:
                        return False
                    else:
                        col_set.add(board[col][row])
        return True