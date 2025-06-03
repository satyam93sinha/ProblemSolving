class Solution:
    # Function to find all possible paths
    def ratInMaze(self, maze):
        # code here
        self.ROWS = self.COLS = len(maze)  # square matrix
        row = col = 0
        self.paths = []
        self.maze = maze
        self.rat_maze_path(row, col, path=[])
        return sorted(self.paths)
    
    def rat_maze_path(self, row, col, path):
        if (row < 0 or col < 0 
            or row >= self.ROWS or col >= self.COLS 
            or self.maze[row][col] == 2 or self.maze[row][col] == 0):
            return
        elif row == self.ROWS-1 and col == self.COLS-1:
            self.paths.append(''.join(path))
            return
        elif self.maze[row][col] == 1:
            self.maze[row][col] = 2
            path.append('D')
            self.rat_maze_path(row+1, col, path)
            path.pop()
            path.append('U')
            self.rat_maze_path(row-1, col, path)
            path.pop()
            path.append('R')
            self.rat_maze_path(row, col+1, path)
            path.pop()
            path.append('L')
            self.rat_maze_path(row, col-1, path)
            path.pop()
            self.maze[row][col] = 1
            
        