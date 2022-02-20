"""
Edge Cases:
1. numRows = 1; return [[1]]
2. numRows = 2; return [[1], [1, 1]]
3. numRows > 2; build Pascal's triangle and return the result
4. numRows = 0; not possible, constraint 1 <= numRows <= 30

Approaches:

Notice -> The number of elements in every row of Pascal's triangle keeps increasing to the length/row number of that Pascal's triangle. 
So, for 1-st row, [1] == pow(11, 0)
for 2nd row,    [1, 1] == pow(11, 1)
3rd row,       [1, 2, 1] == pow(11, 2)
4th row,      [1, 3, 3, 1] == pow(11, 3) and so on ...

1. Brute Force
Declare the result array with required space and then fill in the values based on power of 11(Computation Time: O(logn)) or calculate current row/col value based on the values from previous row, formula:
result[row][col] = result[row-1][col-1] + result[row-1][col]
Time: O(n^2) if we compute values through previous row else O(n^2) * O(logn) if computed based on power of 11.
Space: O(n^2) if considering result space
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for row in range(numRows):
            current_row = [1]
            for col in range(1, row):
                current_row.append(result[row-1][col-1] + result[row-1][col])
            if row > 0:
                current_row.append(1)
            result.append(current_row)
        
        return result
                
                