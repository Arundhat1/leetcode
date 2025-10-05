class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        map = {}
        for i,chara in enumerate(s):
            map[chara] = i
        seen = set()
        res = []
        for i,char in enumerate(s):
            if char in seen:
                continue
            while res and char < res[-1] and map[res[-1]] > i:
                char_to_remove  = res.pop()
                seen.remove(char_to_remove)
            res.append(char)
            seen.add(char)
        return "".join(res)
