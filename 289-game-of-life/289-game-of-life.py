class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_rows, board_cols = len(board), len(board[0])
        # right, left, down, up, left-up-diagonal, right-up-diagonal, left-down-diagonal, right-down-diagonal
        offset = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        # considering 1 changes to dead -1, 0 to live be 2
        for row in range(board_rows):
            for col in range(board_cols):
                count_live = 0
                for offset_row, offset_col in offset:
                    new_row = row + offset_row
                    new_col = col + offset_col
                    if (new_row >= 0 and new_row < board_rows
                       and new_col >= 0 and new_col < board_cols
                       and board[new_row][new_col] in {1, -1}):
                        count_live += 1
                if count_live < 2 and board[row][col] == 1:
                    board[row][col] = -1
                elif count_live > 3 and board[row][col] == 1:
                    board[row][col] = -1
                elif count_live == 3 and board[row][col] == 0:
                    board[row][col] = 2
        
        for row in range(board_rows):
            for col in range(board_cols):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1
        
        