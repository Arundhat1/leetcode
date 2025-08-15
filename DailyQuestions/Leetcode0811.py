class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        def mod_pow(a, e):
            res = 1
            while e > 0:
                if e & 1:
                    res = res * a % MOD
                a = a * a % MOD
                e >>= 1
            return res
        
        def mod_inverse(x):
            return mod_pow(x, MOD - 2)
        
        # Build powers[] from binary representation of n
        powers = []
        bit = 0
        while (1 << bit) <= n:
            if n & (1 << bit):
                powers.append(1 << bit)
            bit += 1
        
        # Prefix products
        prefix = [0] * len(powers)
        for i, val in enumerate(powers):
            prefix[i] = val if i == 0 else (prefix[i - 1] * val) % MOD
        
        # Answer queries
        ans = []
        for L, R in queries:
            if L == 0:
                ans.append(prefix[R])
            else:
                ans.append((prefix[R] * mod_inverse(prefix[L - 1])) % MOD)
        return ans
