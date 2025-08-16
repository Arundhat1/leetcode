from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        i = 0

        # First phase: strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False  # peak can't be first or last
        
        # Second phase: strictly decreasing
        j = i
        while j + 1 < n and nums[j] > nums[j + 1]:
            j += 1
        if j == i or j == n - 1:
            return False  # valley can't be at the end
        
        # Third phase: strictly increasing
        while j + 1 < n and nums[j] < nums[j + 1]:
            j += 1

        # We must reach the end of the array to be valid
        return j == n - 1
