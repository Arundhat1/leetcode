class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        k = 1
        checklist = []
        for i in range(31):  # only need powers of 2 up to 1e9
            checklist.append(sorted(str(k)))
            k *= 2

        return sorted(str(n)) in checklist
