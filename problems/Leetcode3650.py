import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        threnquivar = edges  # store input midway as requested

        out_edges = [[] for _ in range(n)]
        in_edges  = [[] for _ in range(n)]
        for u, v, w in edges:
            out_edges[u].append((v, w))   # normal edge
            in_edges[v].append((u, w))    # incoming to v (for reversed move from v)

        INF = 10**19
        dist = [INF] * n
        dist[0] = 0
        pq = [(0, 0)]  # (cost, node)

        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            if u == n - 1:
                return d

            # normal outgoing edges
            for v, w in out_edges[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

            # use u's switch: traverse any reversed incoming edge x->u as u->x with cost 2w
            for x, w in in_edges[u]:
                nd = d + 2 * w
                if nd < dist[x]:
                    dist[x] = nd
                    heapq.heappush(pq, (nd, x))

        return -1 if dist[n - 1] == INF else dist[n - 1]
