class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = []
        n = len(s)
        for i in range(n):
            long = 0
            subarray = "" 
            for k in range(i,n):
                if s[k] in subarray:
                    
                    break
                else:
                    long += 1
                    subarray = subarray + s[k]
            longest.append(long)
        if n != 0:
            return max(longest)
        else:
            return 0
        
         
        
