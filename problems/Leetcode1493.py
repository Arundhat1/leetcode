from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        blocks = []  # store lengths of consecutive 1's
        
        i = 0
        while i < n:
            if nums[i] == 1:
                length = 0
                while i < n and nums[i] == 1:
                    length += 1
                    i += 1
                blocks.append(length)
            else:
                blocks.append(0)  # mark the zero
                i += 1
        
        # If no 1's at all
        if all(x == 0 for x in blocks):
            return 0
        
        # If all ones only
        if len(blocks) == 1 and blocks[0] != 0:
            return blocks[0] - 1
        
        ans = 0
        for i in range(len(blocks)):
            if blocks[i] != 0:
                ans = max(ans, blocks[i])  # single block
            # merge across a zero
            if i+2 < len(blocks) and blocks[i+1] == 0:
                ans = max(ans, blocks[i] + blocks[i+2])
        
        return ans


        
