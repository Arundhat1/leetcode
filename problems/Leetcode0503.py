from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []  # will store indices

        # loop 2n times to simulate circular array
        for i in range(2 * n - 1, -1, -1):
            j = i % n

            # pop all smaller or equal elements
            while stack and nums[stack[-1]] <= nums[j]:
                stack.pop()

            # only fill answers in the first pass (i < n)
            if i < n:
                if stack:
                    ans[j] = nums[stack[-1]]

            # push this index for future comparisons
            stack.append(j)

        return ans
