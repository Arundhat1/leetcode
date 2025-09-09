class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # length of the shortest string
        j = min(len(s) for s in strs)
        prefix = ""
        
        i = 0
        while i < j:
            check = strs[0][i]
            is_check = True
            for string in strs:
                if i < len(string) and string[i] == check:
                    continue
                else:
                    is_check = False
                    break
            if is_check:
                prefix += check
            else:
                break   # stop once mismatch found
            i += 1
        
        return prefix
