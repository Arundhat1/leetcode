from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # Loop over the first half of the rows in the submatrix
        for r in range(k // 2):
            # Corresponding row from the bottom of the submatrix
            opposite_r = k - 1 - r
            for c in range(k):
                # Swap the elements
                grid[x + r][y + c], grid[x + opposite_r][y + c] = grid[x + opposite_r][y + c], grid[x + r][y + c]
        return grid
