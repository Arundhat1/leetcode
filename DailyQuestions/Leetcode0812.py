class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Precompute all a^x <= n
        powers = []
        a = 1
        while (p := pow(a, x)) <= n:
            powers.append(p)
            a += 1
        
        # Step 2: DP array
        dp = [0] * (n + 1)
        dp[0] = 1  # 1 way to make sum 0
        
        # Step 3: 0/1 Knapsack count
        for p in powers:
            for s in range(n, p - 1, -1):  # go backward to avoid reuse
                dp[s] = (dp[s] + dp[s - p]) % MOD
        
        return dp[n]
