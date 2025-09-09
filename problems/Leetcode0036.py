class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 3x3 sub-boxes

        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == ".":
                    continue

                # Row check
                if x in rows[i]:
                    return False
                rows[i].add(x)

                # Column check
                if x in cols[j]:
                    return False
                cols[j].add(x)

                # Box check
                box_index = (i // 3) * 3 + (j // 3)
                if x in boxes[box_index]:
                    return False
                boxes[box_index].add(x)

        return True
