class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        bitLastSeen = [-1] * 32
        answer = [0] * n

        for i in reversed(range(n)):
            num = nums[i]
            for b in range(32):
                if (num >> b) & 1:
                    bitLastSeen[b] = i

            maxPos = i
            for b in range(32):
                if bitLastSeen[b] != -1:
                    maxPos = max(maxPos, bitLastSeen[b])

            answer[i] = maxPos - i + 1

        return answer




        
