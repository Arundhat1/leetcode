class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # When loop exits, pointers have gone one step too far
            return s[left+1:right]

        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome
            odd_pal = expand_around_center(i, i)
            if len(odd_pal) > len(longest):
                longest = odd_pal

            # Even-length palindrome
            even_pal = expand_around_center(i, i+1)
            if len(even_pal) > len(longest):
                longest = even_pal

        return longest
