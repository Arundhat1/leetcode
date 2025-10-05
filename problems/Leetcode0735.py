class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pos_stk = []  # stack of positive asteroids
        neg_stk = []  # stack of negative asteroids that survive

        for num in asteroids:
            if num > 0:
                pos_stk.append(num)
            else:
                # negative asteroid comes in → it can destroy positives
                while pos_stk and pos_stk[-1] < abs(num):
                    pos_stk.pop()

                if pos_stk and pos_stk[-1] == abs(num):
                    pos_stk.pop()   
                elif not pos_stk:   
                    neg_stk.append(num)

        return neg_stk + pos_stk


