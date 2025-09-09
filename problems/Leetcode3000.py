import math
from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        max_area = 0
        
        for length, width in dimensions:
            # compute diagonal
            diag = math.sqrt(length**2 + width**2)
            # compute area
            area = length * width
            
            # compare diagonals first
            if diag > max_diag:
                max_diag = diag
                max_area = area
            # if diagonals tie, prefer the larger area
            elif diag == max_diag and area > max_area:
                max_area = area
        
        return max_area
