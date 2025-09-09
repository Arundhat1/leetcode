from typing import List
from math import inf

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ones = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1]

        def area(points):
            if not points: 
                return inf
            rmin = min(i for i, _ in points)
            rmax = max(i for i, _ in points)
            cmin = min(j for _, j in points)
            cmax = max(j for _, j in points)
            return (rmax - rmin + 1) * (cmax - cmin + 1)

        best = inf

        # Horizontal 2-cuts
        for i1 in range(1, n-1):
            for i2 in range(i1+1, n):
                g1 = [(i,j) for i,j in ones if i < i1]
                g2 = [(i,j) for i,j in ones if i1 <= i < i2]
                g3 = [(i,j) for i,j in ones if i >= i2]
                best = min(best, area(g1)+area(g2)+area(g3))

        # Vertical 2-cuts
        for j1 in range(1, m-1):
            for j2 in range(j1+1, m):
                g1 = [(i,j) for i,j in ones if j < j1]
                g2 = [(i,j) for i,j in ones if j1 <= j < j2]
                g3 = [(i,j) for i,j in ones if j >= j2]
                best = min(best, area(g1)+area(g2)+area(g3))

        # L-shape: vertical cut + horizontal cut inside left or right part
        for jcut in range(1, m):
            left = [(i,j) for i,j in ones if j < jcut]
            right = [(i,j) for i,j in ones if j >= jcut]

            # split left vertically into 2 horizontal
            for icut in range(1, n):
                g1 = [(i,j) for i,j in left if i < icut]
                g2 = [(i,j) for i,j in left if i >= icut]
                g3 = right
                best = min(best, area(g1)+area(g2)+area(g3))

            # split right vertically into 2 horizontal
            for icut in range(1, n):
                g1 = [(i,j) for i,j in right if i < icut]
                g2 = [(i,j) for i,j in right if i >= icut]
                g3 = left
                best = min(best, area(g1)+area(g2)+area(g3))

        # Symmetric L-shape: horizontal cut + vertical cut inside top/bottom part
        for icut in range(1, n):
            top = [(i,j) for i,j in ones if i < icut]
            bottom = [(i,j) for i,j in ones if i >= icut]

            # split top into 2 vertical parts
            for jcut in range(1, m):
                g1 = [(i,j) for i,j in top if j < jcut]
                g2 = [(i,j) for i,j in top if j >= jcut]
                g3 = bottom
                best = min(best, area(g1)+area(g2)+area(g3))

            # split bottom into 2 vertical parts
            for jcut in range(1, m):
                g1 = [(i,j) for i,j in bottom if j < jcut]
                g2 = [(i,j) for i,j in bottom if j >= jcut]
                g3 = top
                best = min(best, area(g1)+area(g2)+area(g3))

        return best
