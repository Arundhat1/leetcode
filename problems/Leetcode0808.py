class Solution:
    def soupServings(self, n: int) -> float:
        from functools import lru_cache
        
        # Optimization: For large n, probability approaches 1
        if n > 5000:
            return 1.0
        
        @lru_cache(None)  # Built-in memoization, no need for manual dict
        def dfs(a, b):
            # Base cases
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            
            # Recurrence relation
            return 0.25 * (
                dfs(a - 100, b) +
                dfs(a - 75, b - 25) +
                dfs(a - 50, b - 50) +
                dfs(a - 25, b - 75)
            )
        
        return dfs(n, n)
