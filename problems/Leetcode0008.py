class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        i, n = 0, len(s)
        sign = 1
        result = 0

        # 1. Skip leading whitespace
        while i < n and s[i] == " ":
            i += 1

        # 2. Handle optional sign
        if i < n and (s[i] == "+" or s[i] == "-"):
            sign = -1 if s[i] == "-" else 1
            i += 1

        # 3. Convert digits until non-digit is found
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Overflow check before multiplying
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result
