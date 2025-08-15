class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        prev = set()
        for num in arr:
            curr = {num | p for p in prev} | {num}
            result |= curr
            prev = curr
        return len(result)
