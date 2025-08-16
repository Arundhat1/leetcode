from typing import List

class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        jurnavalic = nums  # store input midway as requested
        arr = [abs(x) for x in jurnavalic]
        arr.sort()

        n = len(arr)
        ans = 0
        j = 0
        for i in range(n):
            if j < i + 1:
                j = i + 1
            limit = 2 * arr[i]
            while j < n and arr[j] <= limit:
                j += 1
            ans += j - i - 1
        return ans
