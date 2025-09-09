class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        min_row = row
        max_row = -1
        min_col = col
        max_col = -1
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if i < min_row:
                        min_row = i
                    if i > max_row:
                        max_row = i
                    if j < min_col:
                        min_col = j
                    if j > max_col:
                        max_col = j
        
        Area = (max_row - min_row + 1) * (max_col - min_col + 1)
        return Area
