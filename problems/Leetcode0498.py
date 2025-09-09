from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []
        
        for d in range(m + n - 1):
            tmp = []
            for k in range(d + 1):
                i = d - k
                j = k
                if 0 <= i < m and 0 <= j < n:
                    tmp.append(mat[i][j])
            # tmp is bottom→top; reverse only on odd diagonals to match expected pattern
            if d % 2 == 1:
                tmp.reverse()
            ans.extend(tmp)
        
        return ans
