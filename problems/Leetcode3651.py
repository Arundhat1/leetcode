import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        lurnavrethy = grid  # store input midway as requested

        m, n = len(grid), len(grid[0])
        # cells sorted by value so we can "unlock" all cells <= current value efficiently
        cells = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        cells.sort()

        INF = 10**18
        # dist[i][j][t] = min cost to reach (i,j) having used t teleports
        dist = [[[INF] * (k + 1) for _ in range(n)] for __ in range(m)]
        dist[0][0][0] = 0                        # <-- IMPORTANT: start cost is 0
        pq = [(0, 0, 0, 0)]                      # (cost, i, j, teleports_used)

        # unlock_ptr[t] means how far we've progressed unlocking cells for transitions that produce t+1 teleports-used
        unlock_ptr = [0] * (k + 1)

        while pq:
            cost, i, j, t = heapq.heappop(pq)
            if cost != dist[i][j][t]:
                continue
            if i == m - 1 and j == n - 1:
                return cost

            # normal moves (right, down) — cost is destination cell's value
            for di, dj in ((1, 0), (0, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    nc = cost + grid[ni][nj]
                    if nc < dist[ni][nj][t]:
                        dist[ni][nj][t] = nc
                        heapq.heappush(pq, (nc, ni, nj, t))

            # teleport moves (if still have teleports left)
            if t < k:
                v = grid[i][j]
                # unlock all cells with value <= v for this t (each target cell processed at most once per t)
                while unlock_ptr[t] < len(cells) and cells[unlock_ptr[t]][0] <= v:
                    _, x, y = cells[unlock_ptr[t]]
                    if cost < dist[x][y][t + 1]:
                        dist[x][y][t + 1] = cost
                        heapq.heappush(pq, (cost, x, y, t + 1))
                    unlock_ptr[t] += 1

        return -1
