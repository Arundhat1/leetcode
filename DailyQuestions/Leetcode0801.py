from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            row = [1]  # First element is always 1
            if ans:  # Not the first row
                last_row = ans[-1]
                for j in range(1, i):
                    row.append(last_row[j - 1] + last_row[j])
                row.append(1)  # Last element is also 1
            ans.append(row)
        return ans
