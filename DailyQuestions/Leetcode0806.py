from bisect import bisect_left
from typing import List

class SegmentTree:
    def __init__(self, data):
        n = len(data)
        self.n = n
        self.tree = [float('inf')] * (2 * n)
        for i in range(n):
            self.tree[n + i] = data[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = min(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, idx, value):
        idx += self.n
        self.tree[idx] = value
        while idx > 1:
            idx //= 2
            self.tree[idx] = min(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, left, right):
        res = float('inf')
        left += self.n
        right += self.n
        while left < right:
            if left % 2:
                res = min(res, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                res = min(res, self.tree[right])
            left //= 2
            right //= 2
        return res

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        indexed_baskets = sorted([(b, i) for i, b in enumerate(baskets)])
        original_indices = [i for _, i in indexed_baskets]
        index_to_position = {i: pos for pos, (_, i) in enumerate(indexed_baskets)}

        seg_tree = SegmentTree(original_indices)

        unplaced = 0

        for fruit in fruits:
            # Binary search for first basket with capacity >= fruit
            pos = bisect_left(indexed_baskets, (fruit, -1))  # find first (b >= fruit)
            if pos == len(baskets):
                unplaced += 1
                continue

            # Segment tree gives us the smallest index in this valid range
            min_index = seg_tree.query(pos, len(baskets))
            if min_index == float('inf'):
                unplaced += 1
            else:
                # Basket used; mark it as inf
                used_index = index_to_position[min_index]  # O(1)
  # index in segment tree
                seg_tree.update(used_index, float('inf'))

        return unplaced
