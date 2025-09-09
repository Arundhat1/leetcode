class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        dp[1] = 1  # Day 1, one person knows the secret

        prefix = [0] * (n + 1)
        prefix[1] = 1

        for i in range(2, n + 1):
            start = i - delay
            end = i - forget
            if start >= 1:
                dp[i] = (prefix[start] - (prefix[end] if end >= 1 else 0)) % MOD
            prefix[i] = (prefix[i - 1] + dp[i]) % MOD

        # Count people who still know the secret at day n
        ans = sum(dp[n - forget + 1 : n + 1]) % MOD
        return ans
