from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        best = 0
        
        while i < j:
            h = min(height[i], height[j])
            best = max(best, h * (j - i))
            
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                # equal heights: move either one (moving right is fine too)
                j -= 1
        return best
