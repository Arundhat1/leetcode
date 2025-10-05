from math import gcd

class Solution:
    def replaceNonCoprimes(self, nums):
        def lcm(a, b):
            return a * b // gcd(a, b)

        stack = []
        for num in nums:
            stack.append(num)
            # Keep merging as long as the last two are non-coprime
            while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(lcm(a, b))
        return stack
