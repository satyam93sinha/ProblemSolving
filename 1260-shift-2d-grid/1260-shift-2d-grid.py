class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if k == 0:
            return grid
        rows, cols = len(grid), len(grid[0])
        answer_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
        for _ in range(k):
            for row in range(rows):
                for col in range(cols):
                    if col < cols-1:
                        answer_matrix[row][(col+1)%cols] = grid[row][col]
                    else:
                        answer_matrix[(row+1)%rows][0] = grid[row][col]
            grid = [[answer_matrix[row][col] for col in range(cols)] for row in range(rows)]
        return answer_matrix