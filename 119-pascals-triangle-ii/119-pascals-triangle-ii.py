class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        row = [1, 1]
        for rows in range(2, rowIndex+1):
            current_row = [1]
            for cols in range(1, rows):
                current_row.append(row[cols-1] + row[cols])
            current_row.append(1)
            row = current_row.copy()
        
        return row
        