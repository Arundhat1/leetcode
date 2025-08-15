from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        total = Counter()

        # Step 1: Combine counts and check for feasibility
        for fruit in set(basket1 + basket2):
            total[fruit] = count1[fruit] + count2[fruit]
            if total[fruit] % 2 != 0:
                return -1  # Can't split odd total count

        # Step 2: Determine what to move from both baskets
        from1, from2 = [], []

        for fruit in total:
            diff = count1[fruit] - count2[fruit]
            if diff > 0:
                from1.extend([fruit] * (diff // 2))
            elif diff < 0:
                from2.extend([fruit] * (-diff // 2))

        # Step 3: Sort to minimize swap cost
        from1.sort()
        from2.sort(reverse=True)
        global_min = min(basket1 + basket2)
        cost = 0

        for a, b in zip(from1, from2):
            cost += min(min(a, b), 2 * global_min)

        return cost

