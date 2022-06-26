"""
Edge Cases:
1. Empty grid; no islands, return 0
2. grid contains only one island; return 1
    2.1 whole grid is an island
    2.2 there's just single island surrounded by water
3. grid contains multiple islands
4. grid contains no island, only water

Test Cases:
[[]]
[["1"]]
[["1", "1", "1"], ["1", "1", "1"]]
[["0", "1", "0"], ["0", "1", "0"]]
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
[["0", "0"], ["0", "0"]]

Approaches:
Let's assume we are not allowed to modify the grid
1. BFS -> Thanks to NeetCode!!
Intuition:
Solve manually first, however you wish to solve it.
Which directions to go to, in search of island?
-> Up, Down, Left and Right
Explore the first row, col provided then move on to the next row, col got through the earlier one -> BFS
Time: O(m x n)
Space: O(m x n)

2. DFS -> Thanks to TechDose!!
Intuition:
Simple, go through the row, col and perform dfs on each of them in the allowed directions.
Time: O(m x n)
Space: O(m x n)

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row, col):
            # dfs means recursive or stack data structure can be used
            visited.add((row, col))
            # up, down, left, right
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            
            for delta_row, delta_col in directions:
                new_row, new_col = row + delta_row, col + delta_col
                # ensure new_row and new_col are within array bounds,
                # grid element at this new location is "1",
                # and not yet visited
                if (0 <= new_row < rows 
                    and 0 <= new_col < cols
                    and grid[new_row][new_col] == "1"
                    and (new_row, new_col) not in visited):
                    dfs(new_row, new_col)
        
        def bfs(row, col):
            # bfs means use a queue data structure
            queue = collections.deque()
            queue.append((row, col))
            visited.add((row, col))
            # up, down, left, right directions
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            
            while queue:
                row, col = queue.popleft()
                for delta_row, delta_col in directions:
                    new_row, new_col = row + delta_row, col + delta_col
                    # ensure new_row, new_col are within array bounds,
                    # grid element at this new location is "1",
                    # and not yet visited
                    if (0 <= new_row < rows 
                        and 0 <= new_col < cols 
                        and grid[new_row][new_col] == "1"
                        and (new_row, new_col) not in visited):
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
        
        if not grid:
            return 0
        # grid is present, not empty
        # will have to iterate over the grid to find the number of islands
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set() # contains the combination of (row, col)
        
        for row in range(rows):
            for col in range(cols):
                # grid element is "1" and not yet visited
                if grid[row][col] == "1" and (row, col) not in visited:
                    # perform a bfs to search for adjacent land and count them as
                    # single island
                    # bfs(row, col)
                    # now, perform a dfs to search for adjacent land and count them as
                    # single island
                    dfs(row, col)
                    islands += 1
        # return total number of islands found
        return islands
        
        