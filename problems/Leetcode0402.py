class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []

        for char in num:

            while stk and k > 0 and stk[-1] > char:
                stk.pop()
                k -= 1
            stk.append(char)


        while k > 0:
            stk.pop()
            k -= 1
        first_non_zero = -1
        n =len(stk)
        for i in range(n):
            if stk[i] != '0':
                first_non_zero = i
                break
        if first_non_zero != -1:
            stk = stk[first_non_zero :]
        else:
            return '0'

        result = "".join(stk)

        return result if result else "0"

