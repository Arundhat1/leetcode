class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c0 = c1 = c2 = 0
        for i in nums:
            if i == 0:
                c0 += 1
            elif i == 1:
                c1 += 1
            else:
                c2 += 1

    # Overwrite nums in-place
        for i in range(c0):
            nums[i] = 0
        for i in range(c0, c0 + c1):
            nums[i] = 1
        for i in range(c0 + c1, len(nums)):
            nums[i] = 2
